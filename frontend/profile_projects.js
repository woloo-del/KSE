(function(host){
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const labels = {all:'Wszystkie opublikowane wpisy',conditions:'Wydane warunki',agreements:'Obowiązujące umowy',applications:'Wnioski',refusals:'Odmowy'};
  function category(status){
    if(status==='WARUNKI PRZYŁĄCZENIA wydane') return 'conditions';
    if(status==='UMOWA O PRZYŁĄCZENIE obowiązująca') return 'agreements';
    if(status==='ODMOWA PRZYŁĄCZENIA') return 'refusals';
    if(status.startsWith('WNIOSEK ')) return 'applications';
    return 'unknown';
  }
  function filter(rows,kind,query=''){
    const q=query.trim().toLocaleLowerCase('pl');
    return rows.filter(row => (kind==='all'||category(row.status_reported)===kind) &&
      (!q||[row.applicant,row.project_name].some(v=>String(v??'').toLocaleLowerCase('pl').includes(q))));
  }
  function power(value,raw){
    return value===null || value===undefined ? 'Nieustalona'+(raw===null || raw===undefined?'':' · zapis źródłowy: '+esc(raw)) : esc(value)+' MW';
  }
  function cards(rows,provenance){
    if(!rows.length) return '<p class="empty">Brak wpisów dla tych filtrów w zachowanej publikacji. Nie oznacza to braku projektów.</p>';
    return rows.map(r=>'<article class="evidence project-card"><span class="tag sage">'+esc(r.status_reported)+'</span>'+ 
      '<h3>'+esc(r.project_name||'Nazwa obiektu niepodana')+'</h3><p><strong>Podmiot wg PSE: </strong>'+esc(r.applicant||'Nie podano')+'</p>'+
      '<dl class="project-values"><div><dt>Technologia wg źródła</dt><dd>'+esc(r.technology_reported||'Nie podano')+'</dd></div>'+
      '<div><dt>Moc wprowadzana</dt><dd>'+power(r.export_MW,r.raw_export)+'</dd></div><div><dt>Moc pobierana</dt><dd>'+power(r.import_MW,r.raw_import)+'</dd></div></dl>'+
      '<details><summary>Inwestor i dowód źródłowy</summary><p>Publikacja podaje nazwę podmiotu. Nie rozstrzyga tu roli właściciela końcowego, dewelopera ani przynależności do grupy.</p>'+
      '<dl class="project-values"><div><dt>KRS / NIP</dt><dd>Nie zweryfikowano</dd></div><div><dt>Grupa inwestorska i właściciele</dt><dd>Nie ustalono</dd></div></dl>'+
      '<p>Potrzebne do uzupełnienia: jednoznaczny wpis rejestrowy tej spółki oraz datowane źródło powiązania z grupą.</p>'+
      '<p class="quiet">PSE · REPORTED · stan '+esc(provenance.pipeline_source_date)+' · arkusz „Wykaz wspólny”, wiersz '+esc(r.row)+'. Punkt: '+esc(r.point_reported)+' · '+esc(r.voltage_reported)+' kV.</p>'+
      '<p class="quiet">'+(r.review_reasons.length?'Do sprawdzenia: '+r.review_reasons.map(esc).join(', '):'Brak ostrzeżeń parsera nie oznacza ręcznej weryfikacji.')+'</p></details></article>').join('');
  }
  const api={category,filter,cards,labels};
  if(typeof module==='object'&&module.exports) module.exports=api; else host.KSEProfileProjects=api;
})(globalThis);
