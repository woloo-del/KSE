(function (host) {
  'use strict';
  const version = 'profile_review_v2';
  function coverage(profile) {
    return [
      {section:'Projekty i podmioty',status:'PARTIAL',description:'Wiersze jednego wykazu PSE; nie jest to pełny rejestr inwestycji. Warunki i umowa nie potwierdzają uruchomienia.'},
      {section:'Tożsamość inwestorów',status:'UNKNOWN',description:'Nazwa podmiotu wg PSE; brak zweryfikowanego KRS/NIP, właścicieli i grupy inwestorskiej.'},
      {section:'Inwestycje sieciowe',status:profile.links.length?'PARTIAL':'UNKNOWN',description:'Indeks nagłówków portalu. Dopasowanie nazwy nie potwierdza zakresu ani tożsamości stacji.'},
      {section:'Instalacje pracujące',status:'UNKNOWN',description:'Brak kompletnego wykazu uruchomionych instalacji dla tego profilu.'},
      {section:'Topologia i grunty',status:'NOT_INTEGRATED',description:'Dane pilota i analizy GIS nie zostały powiązane z tym profilem.'}
    ];
  }
  const noteKey = id => 'kse:profile-note:v1:' + id;
  const opinion = profile => profile.links.some(link => link.direct)
    ? 'Są opisy zadań odnoszące się wprost do nazwy stacji. Ich status, zakres napięć i związek z wybranym punktem wymagają weryfikacji przed uznaniem modernizacji za korzystną przesłankę.'
    : 'Zebrane materiały nie wystarczają do określenia znaczenia inwestycji dla tego punktu. Brak dopasowania nie oznacza braku planów rozwoju.';

  function build(data, profileId, note, generatedAt) {
    const p = data.profiles.find(profile => profile.id === profileId);
    if (!p || typeof note !== 'string' || note.length > 20000 || !Number.isFinite(Date.parse(generatedAt))) throw Error('INVALID_REPORT_INPUT');
    return JSON.parse(JSON.stringify({
      report_version: version, generated_at: generatedAt,
      scope: data.scope, profile: {id:p.id, name:p.name, voltage_kV:p.voltage, identity_status:'UNVERIFIED_SOURCE_PROFILE'},
      pipeline: {record_count:p.count, status_counts:p.statuses, parser_review_count:p.reviewCount,
        scope:'SOURCE_ROWS_NOT_UNIQUE_PROJECTS', operational_coverage:'UNKNOWN', pending_applications_coverage:'UNKNOWN'},
      projects:p.projects || [], pipeline_footnotes:data.pipeline_footnotes || [],
      investor_scope:'APPLICANT_REPORTED_BY_PSE_NOT_VERIFIED_OWNER_OR_GROUP',
      coverage:coverage(p),
      investments:p.links.map(link => ({heading_id:link.id, ...data.headings[link.id],
        relationship:link.direct ? 'EXPLICIT_STATION_NAME_IDENTITY_UNVERIFIED' : 'OTHER_CONTEXT_REQUIRES_REVIEW'})),
      interpretation: {classification:'UNKNOWN', text:opinion(p)},
      gaps:['Tożsamość stacji i zakres napięć wymagają potwierdzenia.',
        'Brak pełnej listy projektów operacyjnych i wniosków oczekujących; nie oznacza to zera.',
        'Znaczenie inwestycji dla punktu, kierunku import/eksport i terminu projektu wymaga oceny.',
        'Moduł gruntów nie jest jeszcze zintegrowany z tą kartą.'],
      provenance:data.provenance,
      user_note:{text:note, classification:'USER_INPUT_NOT_SOURCE_EVIDENCE'},
      limits:['Brak oceny możliwości przyłączenia, wolnych MW, obciążenia, score lub prawdopodobieństwa.',
        'Raport używa zachowanych publikacji; wygenerowanie raportu nie odświeża źródeł.']
    }));
  }

  function markdown(report) {
    const p=report.profile;
    const lines=['# Karta przeglądu: '+p.name+' · '+p.voltage_kV+' kV','',
      'Wygenerowano: '+report.generated_at,'Profil źródłowy — tożsamość stacji niepotwierdzona.','',
      '## Opublikowane projekty','',
      'Stan wykazu: '+report.provenance.pipeline_source_date,
      'Liczba wierszy publikacji: '+report.pipeline.record_count,''];
    for(const [status,count] of Object.entries(report.pipeline.status_counts)) lines.push('- '+status+': '+count);
    lines.push('','## Szczegóły projektów i podmiotów','',
      'Podmiot według PSE; KRS/NIP, grupa i właściciele nie zostały zweryfikowane. Moce to wartości z wykazu, nie rezerwa ani obciążenie sieci.');
    for(const row of report.projects) lines.push('', '### '+(row.project_name||'Nazwa niepodana'),
      'Podmiot wg PSE: '+(row.applicant||'Nie podano'), 'Status: '+row.status_reported,
      'Technologia: '+(row.technology_reported||'Nie podano'),
      'Moc wprowadzana: '+(row.export_MW===null?'nieustalona; zapis źródłowy: '+(row.raw_export??'brak'):row.export_MW+' MW'),
      'Moc pobierana: '+(row.import_MW===null?'nieustalona; zapis źródłowy: '+(row.raw_import??'brak'):row.import_MW+' MW'),
      'Źródło: Wykaz wspólny, wiersz '+row.row+'; REPORTED.',
      'Ostrzeżenia parsera: '+(row.review_reasons.join(', ')||'brak; nie oznacza ręcznej weryfikacji'));
    lines.push('','## Pokrycie danych','',...report.coverage.map(c=>'- '+c.section+': '+c.description));
    if(report.pipeline_footnotes.length) lines.push('','## Przypisy publikacji PSE','',...report.pipeline_footnotes.map(f=>'- '+f.marker+' '+f.meaning));
    lines.push('','## Wzmianki o inwestycjach','');
    if(!report.investments.length) lines.push('Brak dopasowań w zachowanym indeksie; nie oznacza braku inwestycji.');
    for(const item of report.investments) lines.push('- '+item.title,
      '  Status raportowany: '+(item.status || 'nieustalony'),
      '  Powiązanie: '+(item.relationship==='EXPLICIT_STATION_NAME_IDENTITY_UNVERIFIED'?'nazwa stacji w opisie, tożsamość niepotwierdzona':'inny kontekst, wymaga sprawdzenia')+'; lokalizator h4: '+item.positions.join(', '));
    lines.push('','## Interpretacja aplikacji — niewiadome','',report.interpretation.text,
      '','## Braki i ograniczenia','',...report.gaps.map(x=>'- '+x),...report.limits.map(x=>'- '+x),
      '','## Notatka użytkownika — nie jest dowodem źródłowym','',report.user_note.text || '(brak notatki)',
      '','## Źródła, daty i wersje','', 'Wersja raportu: '+report.report_version,'',
      '```json',JSON.stringify(report.provenance,null,2),'```','');
    return lines.join('\n');
  }

  function readNote(storage,id) {
    try { const raw=storage.getItem(noteKey(id)); if(raw===null) return {text:'',state:'empty'};
      const note=JSON.parse(raw);
      if(note.profile_id!==id || typeof note.text!=='string' || note.text.length>20000) throw Error('INVALID_NOTE');
      return {text:note.text,state:'saved'};
    } catch {return {text:'',state:'unavailable'};}
  }
  function saveNote(storage,id,text) {
    if(typeof text!=='string' || text.length>20000) throw Error('INVALID_NOTE');
    storage.setItem(noteKey(id),JSON.stringify({profile_id:id,text}));
  }
  const api={build,markdown,opinion,readNote,saveNote,coverage};
  if(typeof module==='object' && module.exports) module.exports=api;
  else host.KSEProfileReport=api;
})(globalThis);
