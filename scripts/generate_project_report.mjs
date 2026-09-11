import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
import {collect, todoMarkdown, documentRows, plain, STATUS, sha} from './report_data.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const require=createRequire(path.join(root,'.report_runtime','anchor.cjs'));
const {Workbook, SpreadsheetFile, FileBlob}=await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const artifactVersion=JSON.parse(await fs.readFile(path.join(root,'.report_runtime/node_modules/@oai/artifact-tool/package.json'),'utf8')).version;
const data=await collect(root);
await fs.writeFile(path.join(root,'TODO.md'),todoMarkdown(data),'utf8');
const templatePath='data/reference/project_tracker_template.xlsx';
const templateBytes=await fs.readFile(path.join(root,templatePath));
for(const relative of ['scripts/report_data.mjs','scripts/generate_project_report.mjs','scripts/generate_project_report.ps1','scripts/validate_project_report.py',templatePath]) {
  const b=await fs.readFile(path.join(root,relative)); data.inputs.push({path:relative,sha256:sha(b),bytes:b.length});
}
data.fingerprint=sha(JSON.stringify(data.inputs));
const outDir=path.join(root,'outputs','01a08b04-7ddd-7641-8f44-7d0d6ae13653');
const stem=`raport_projektu_KSE_${data.todo.updated_at}_${data.fingerprint.slice(0,10)}`;
const previewDir=path.join(outDir,'previews',stem);
await fs.mkdir(outDir,{recursive:true});
await fs.mkdir(previewDir,{recursive:true});
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(path.join(root,templatePath)));
const skipPreviews=process.argv.includes('--skip-previews');
if(!skipPreviews) {
  const before=await wb.render({sheetName:'Project Plan',range:'B2:AD14',scale:1,format:'png'});
  await fs.writeFile(path.join(previewDir,'00_template.png'),new Uint8Array(await before.arrayBuffer()));
}
console.log('Imported Project Tracker reference; preparing report.');

const sheets={};
for(const name of ['Podsumowanie','TODO','Wykonalność','Źródła','Źródła szczegóły','Ryzyka','Dokumentacja','Audyt','Odtwarzanie']) sheets[name]=wb.worksheets.add(name);
const rendered=[];
function literal(value) {
  if(value===null||value===undefined) return 'Nie ustalono';
  if(typeof value==='string') {
    if(/^\d{4}-\d{2}-\d{2}(T[\d:.]+(Z|[+-]\d{2}:\d{2}))?$/.test(value)) return new Date(value);
    return value.startsWith('=')?"'"+value:value;
  }
  return value;
}
function label(n) {let s='';for(n++;n>0;n=Math.floor((n-1)/26)) s=String.fromCharCode(65+(n-1)%26)+s;return s;}
function height(values,widths) {
  return Math.max(30,...values.map((v,i)=>Math.ceil(String(v??'').length/Math.max(10,widths[i]-4))*14+10));
}
function table(name,title,headers,rows,widths,note='') {
  const s=sheets[name]; const end=rows.length+6, last=label(headers.length-1);
  s.showGridLines=false;
  s.getRange(`A1:${last}${end}`).format.font={name:'Arial',size:10,color:'#222238'};
  s.getRange(`A1:${last}${end}`).format.verticalAlignment='top';
  headers.forEach((_,i)=>s.getRange(`${label(i)}1:${label(i)}${end}`).format.columnWidth=widths[i]);
  s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#3D308C'};
  s.getRange(`A2:${last}2`).format.rowHeight=30;
  s.getRange(`A3:${last}3`).format.borders={bottom:{style:'thin',color:'#7765C8'}};
  if(note) {s.getRange('A4').values=[[note]];s.getRange('A4').format.font={name:'Arial',size:10,italic:true,color:'#535269'};}
  s.getRange(`A6:${last}${end}`).values=[headers,...rows.map(r=>r.map(literal))];
  const t=s.tables.add(`A6:${last}${end}`,true,`ReportTable${Object.keys(sheets).indexOf(name)+1}`);
  t.showFilterButton=true;
  t.style='TableStyleLight1';
  rows.forEach((row,i)=>row.forEach((value,j)=>{
    if(literal(value) instanceof Date) s.getRange(`${label(j)}${i+7}`).setNumberFormat(value.includes('T')?'yyyy-mm-dd hh:mm:ss "UTC"':'yyyy-mm-dd');
  }));
  s.getRange(`A6:${last}6`).format={fill:'#44338F',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,verticalAlignment:'center',horizontalAlignment:'center',rowHeight:34};
  s.getRange(`A7:${last}${end}`).format.wrapText=true;
  rows.forEach((row,i)=>s.getRange(`A${i+7}:${last}${i+7}`).format.rowHeight=Math.min(400,height(row,widths)));
  s.freezePanes.freezeRows(6);
  if(headers.length>4) s.freezePanes.freezeColumns(2);
  return s;
}
function dateCells(sheet,column,values) {
  values.forEach((d,i)=>{if(d) sheet.getRange(`${column}${i+7}`).values=[[new Date(d)]];else sheet.getRange(`${column}${i+7}`).values=[[null]];});
  sheet.getRange(`${column}7:${column}${values.length+6}`).setNumberFormat('yyyy-mm-dd');
}
const tasks=data.tasks;
const todoRows=tasks.map(t=>[t.id,t.title,t.status,t.priority,t.stage,t.owner,t.depends_on.join(', ')||'Brak',t.unmet_dependencies.join(', ')||'Brak',t.next_action,t.acceptance,t.risk||'Brak dodatkowej uwagi',t.due_date??null,t.completed_at??null,(t.evidence??[]).join('\n')]);
const todo=table('TODO','Rejestr zadań', ['ID','Zadanie','Status','Priorytet','Etap','Odpowiedzialność','Zależności','Nieukończone zależności','Następny krok','Kryterium zakończenia','Ryzyko / uwaga','Termin docelowy','Zakończono','Dowody i kontekst'],todoRows,[14,48,18,11,18,26,28,28,65,75,65,18,18,60],'Statusy: Complete = zrobione; In Progress = w toku; Not Started = do zrobienia; At Risk = zagrożone.');
dateCells(todo,'L',tasks.map(t=>t.due_date));dateCells(todo,'M',tasks.map(t=>t.completed_at));
todo.getRange(`C7:C${tasks.length+6}`).dataValidation={rule:{type:'list',values:Object.keys(STATUS)}};
for(const [status,fill,color] of [['At Risk','#FCE3E5','#A41F35'],['In Progress','#E6E1FF','#44338F'],['Complete','#E2F1EB','#246653']]) todo.getRange(`C7:C${tasks.length+6}`).conditionalFormats.add('containsText',{text:status,format:{fill,font:{color,bold:true}}});

const plan=wb.worksheets.getItem('Project Plan');
plan.getRange('B10:H39').clear({applyTo:'contents'});
const ranked=[...tasks].sort((a,b)=>(a.status==='Complete')-(b.status==='Complete')||a.priority.localeCompare(b.priority)||a.id.localeCompare(b.id));
const view=ranked.slice(0,30);
plan.getRange(`B10:H${9+view.length}`).values=view.map(t=>[t.stage,`${t.id} ${t.title}`,t.owner,t.status,t.priority,t.started_at?new Date(t.started_at):null,(t.completed_at||t.due_date)?new Date(t.completed_at||t.due_date):null]);
for(const [cell,value] of Object.entries({'B2':'KSE — plan prac i raport projektu','S2':'Grid Connection Intelligence','B4':'PROJEKT','K4':'STAN ZADAŃ','B5':'Nazwa','C5':'Grid Connection Intelligence','F5':'Koordynacja','H5':'Użytkownik + Codex','B6':'Obszar','C6':'Polska','F6':'Oś od tygodnia','B8':'PLAN PRAC','K8':'OŚ CZASU — TYLKO USTALONE DATY','B9':'Etap','C9':'Zadanie','D9':'Odpowiedzialność','E9':'Status','F9':'Priorytet','G9':'Początek','H9':'Koniec','I9':'Dni','K5':'WSZYSTKIE','O5':'ZROBIONE','S5':'W TOKU','W5':'ZAGROŻONE','AA5':'PRIORYTET P0'})) plan.getRange(cell).values=[[value]];
const monday=new Date(data.todo.updated_at+'T00:00:00Z');monday.setUTCDate(monday.getUTCDate()-(monday.getUTCDay()+6)%7);
plan.getRange('H6').values=[[monday]];
// Re-register imported formulas so stale template caches cannot survive changed inputs.
plan.getRange('I10:I39').clear({applyTo:'contents'});
plan.getRange('K9:AD39').clear({applyTo:'contents'});
plan.getRange('K9:AD9').formulas=[Array.from({length:20},(_,i)=>i?`=${label(i+9)}9+7`:'=$H$6')];
for(let r=10;r<=39;r++) {
  plan.getRange(`I${r}`).formulas=[[`=IF(OR(G${r}="",H${r}="",H${r}<G${r}),"",H${r}-G${r}+1)`]];
  plan.getRange(`K${r}:AD${r}`).formulas=[Array.from({length:20},(_,i)=>`=IF(OR($G${r}="",$H${r}="",$H${r}<$G${r}),"",IF(AND(${label(i+10)}$9<=$H${r},${label(i+10)}$9+6>=$G${r}),1,""))`)];
}
plan.getRange('G10:H39').setNumberFormat('dd mmm yy');
plan.getRange('B10:H39').format.wrapText=true;plan.getRange('B10:AD39').format.rowHeight=48;
plan.getRange('B10:B39').dataValidation={rule:{type:'list',values:[...new Set(tasks.map(t=>t.stage))]}};
plan.getRange('D10:D39').dataValidation={rule:{type:'list',values:[...new Set(tasks.map(t=>t.owner))]}};
const lastTask=tasks.length+6;
for(const [cell,formula] of Object.entries({'K6':`=COUNTA('TODO'!A7:A${lastTask})`,'O6':`=COUNTIFS('TODO'!C7:C${lastTask},"Complete")`,'S6':`=COUNTIFS('TODO'!C7:C${lastTask},"In Progress")`,'W6':`=COUNTIFS('TODO'!C7:C${lastTask},"At Risk")`,'AA6':`=COUNTIFS('TODO'!D7:D${lastTask},"P0")`})) plan.getRange(cell).formulas=[[formula]];
plan.getRange('B41').values=[['Widok do 30 zadań. Pełny rejestr i zależności: TODO. Brak ustalonych dat oznacza brak paska. Zmiany trwałe zapisujemy w JSON i ponownie generujemy raport.']];
plan.getRange('B41:AD42').format.wrapText=true;
plan.freezePanes.freezeRows(9);plan.freezePanes.freezeColumns(3);

const sources=data.catalog.sources;
table('Źródła','Katalog źródeł', ['ID źródła','Źródło','Operator / właściciel','Kategoria','Weryfikacja','Sprawdzono','API','GIS','Użycie komercyjne','Priorytet'],sources.map(s=>[s.source_id,s.source_name,s.operator||s.data_owner,s.data_category,s.verification_status,s.last_verified,s.api_available,s.gis_available,s.commercial_use,s.priority]),[29,58,35,32,29,18,28,32,38,12],'Weryfikacja próbki nie oznacza pełnej walidacji zbioru. Linki i wszystkie pola: Źródła szczegóły.');
dateCells(sheets['Źródła'],'F',sources.map(s=>s.last_verified));
const details=[];
for(const s of sources) for(const [field,value] of Object.entries(s)) {
  const text=value===null?'UNKNOWN — nie ustalono':typeof value==='object'?JSON.stringify(value,null,2):String(value);
  const chunks=documentRows('',text).map(r=>r[2]);
  (chunks.length?chunks:['Brak pozycji']).forEach((chunk,i)=>details.push([s.source_id,field+(chunks.length>1?` (${i+1}/${chunks.length})`:''),chunk]));
}
table('Źródła szczegóły','Pełne pola i dowody źródeł',['ID źródła','Pole','Wartość / wyjaśnienie'],details,[30,40,120],'Filtruj po ID źródła lub polu. UNKNOWN jest brakiem wiedzy, a nie zerem.');
table('Wykonalność','Co można wiarygodnie ustalić',['Funkcja / wielkość','Klasa','Dowód i warunek','Granica / brak danych'],data.feasibility,[65,34,85,85],'Ocena dostępności danych, nie lista wdrożonych funkcji.');

const riskRows=[];
for(const s of sources) {
  if(['BLOCKED','DISCOVERED'].includes(s.verification_status)) riskRows.push([s.source_id,'Dostęp / treść',s.verification_status,s.known_limitations.join(' '),'Utrzymać oznaczenie do udanego odczytu.']);
  if(s.date_conflict) riskRows.push([s.source_id,'Konflikt dat','Nierozstrzygnięty',JSON.stringify(s.date_conflict),'Porównać źródła; nie rozstrzygać po nazwie pliku.']);
  if(s.commercial_use==='UNKNOWN'||s.commercial_use==='REQUIRES_PERMISSION_REVIEW') riskRows.push([s.source_id,'Prawa do wykorzystania',s.commercial_use,s.license,'Wyjaśnić zakres przed produkcyjnym użyciem.']);
}
for(const t of tasks.filter(t=>t.risk)) riskRows.push([t.id,'Zadanie',STATUS[t.status],t.risk,t.next_action]);
table('Ryzyka','Ograniczenia wymagające dalszej pracy',['ID','Obszar','Stan','Wyjaśnienie','Dalsze działanie'],riskRows,[30,28,32,100,75],'Jedno źródło może mieć kilka różnych ograniczeń. Liczba wierszy nie jest liczbą unikalnych źródeł.');

const documentation=Object.entries(data.docs).flatMap(([name,text])=>documentRows(name,text));
table('Dokumentacja','Pełne wyjaśnienia, założenia i decyzje',['Dokument','Sekcja','Treść'],documentation,[42,55,130],'Filtruj po dokumencie lub sekcji. Długie akapity są dzielone na kolejne wiersze bez pomijania treści.');

const auditRows=[['Walidacja badania','Data wykonania',data.validation.checked_at_utc],['Walidacja badania','Wynik zapisany',data.validation.status],['Walidacja badania','Zakres',data.validation.scope]];
for(const w of data.validation.source_warnings) auditRows.push([w.source_id,w.code,w.message]);
for(const c of data.validation.checks) auditRows.push(['Kontrola lokalna',c.name,`${c.passed?'PASS':'FAIL'}${c.detail===null?'':': '+JSON.stringify(c.detail)}`]);
table('Audyt','Zapisane wyniki kontroli badania',['Grupa / źródło','Kontrola','Wynik / wyjaśnienie'],auditRows,[30,85,110],'To zapis wcześniejszych kontroli z podaną datą, nie potwierdzenie aktualnego stanu zdalnych serwisów.');

const executive=documentRows('docs/01_data_research.md',data.docs['docs/01_data_research.md']).filter(r=>r[1]==='1. Executive summary');
const summaryRows=[['Źródła w katalogu',null,'Obejmuje próbki, przegląd treści/dokumentacji, wskazania i blokady.'],['Zadania w rejestrze',null,'Pełna lista, także zakończone i dalsze etapy.'],['Zakończone zadania',null,'Liczba zadań nie mierzy procentowej gotowości produktu.'],['Zadania w toku',null,'Stan zapisany w rejestrze TODO.'],['Zadania zagrożone',null,'Odrębne od nieukończonych zależności.'],['Data katalogu',data.catalog.as_of,'Data przeglądu źródeł; nie oznacza aktualnego stanu każdego dokumentu.'],...executive.map(r=>['Wniosek z badań','Ocena badawcza',r[2]])];
table('Podsumowanie','Stan projektu i najważniejsze wnioski',['Obszar','Wynik','Znaczenie i ograniczenia'],summaryRows,[35,27,125],'Raport wiedzy projektowej. Nie zawiera obliczonej rezerwy MW ani Grid Connection Score dla konkretnego GPZ.');
for(const [cell,formula] of Object.entries({'B7':`=COUNTA('Źródła'!A7:A${sources.length+6})`,'B8':"='Project Plan'!K6",'B9':"='Project Plan'!O6",'B10':"='Project Plan'!S6",'B11':"='Project Plan'!W6"})) sheets['Podsumowanie'].getRange(cell).formulas=[[formula]];
sheets['Podsumowanie'].getRange('B12').values=[[new Date(data.catalog.as_of)]];sheets['Podsumowanie'].getRange('B12').setNumberFormat('yyyy-mm-dd');
sheets['Podsumowanie'].tabColor='#44338F';

const runtimeRows=[['Wygenerowano UTC',new Date().toISOString()],['Stan rejestru TODO',data.todo.updated_at],['Commit widoczny przy generowaniu',data.git],['SHA-256 zestawu wejść',data.fingerprint],['Node.js',process.version],['artifact-tool',artifactVersion],['Szablon','Project Tracker — zachowana struktura planu; dane demonstracyjne zastąpione'],['SHA-256 szablonu',sha(templateBytes)],['Źródło zadań','data/project/todo.json; Excel i TODO.md są widokami generowanymi'],['Odświeżenie','Uruchom scripts/generate_project_report.ps1 w folderze projektu.'],['Historia źródeł','Do odtworzenia dokładnych źródeł potrzebne archiwum ZIP i zgodny manifest w repozytorium.'],['SHA-256 archiwum badania',data.archive.archive_sha256],['Sekrety','Generator nie odczytuje _secrets ani tokenów.'],['Edycja Excela','Zmiany w XLSX nie wracają do rejestru; wprowadź je do właściwych plików i wygeneruj ponownie.'],...data.inputs.map(i=>[i.path,`SHA-256 ${i.sha256}; ${i.bytes} bajtów`])];
table('Odtwarzanie','Pochodzenie raportu i ponowne generowanie',['Element','Wartość / instrukcja'],runtimeRows,[70,130],'Hashe wskazują dokładne wejścia, także gdy podczas generowania nie były jeszcze w commicie.');

// Test a representative live formula dependency and restore the original value.
wb.recalculate();
const done=tasks.filter(t=>t.status==='Complete').length;
assert.equal(plan.getRange('O6').values[0][0],done);
const original=todo.getRange('C7').values[0][0];
todo.getRange('C7').values=[['Not Started']];wb.recalculate();
assert.equal(plan.getRange('O6').values[0][0],done-(original==='Complete'?1:0));
todo.getRange('C7').values=[[original]];
wb.recalculate();
assert.equal(plan.getRange('O6').values[0][0],done);
assert.equal(sheets['Podsumowanie'].getRange('B7').values[0][0],sources.length);
const inspection=await wb.inspect({kind:'table',range:'Podsumowanie!A6:C12',include:'values,formulas',tableMaxRows:7,tableMaxCols:3,maxChars:2500});
const errorScan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'formula errors',maxChars:3000});
await fs.writeFile(path.join(outDir,stem+'.inspection.json'),JSON.stringify({inspection:inspection.ndjson,errorScan:errorScan.ndjson},null,2));
console.log(inspection.ndjson);console.log(errorScan.ndjson);
if(!skipPreviews) {
  const ranges={'Project Plan':'B2:AD16','Podsumowanie':'A2:C13','TODO':'A2:F10','Wykonalność':'A2:D9','Źródła':'A2:F10','Źródła szczegóły':'A2:C12','Ryzyka':'A2:E9','Dokumentacja':'A2:C9','Audyt':'A2:C11','Odtwarzanie':'A2:B12'};
  for(const [name,range] of Object.entries(ranges)) {
    const png=await wb.render({sheetName:name,range,scale:1,format:'png'});
    const filename=String(rendered.length+1).padStart(2,'0')+'_'+name.replaceAll(' ','_')+'.png';
    await fs.writeFile(path.join(previewDir,filename),new Uint8Array(await png.arrayBuffer()));
    rendered.push({sheet:name,range,file:path.relative(root,path.join(previewDir,filename)).replaceAll('\\','/')});
    console.log('Preview:',name);
  }
}
const file=await SpreadsheetFile.exportXlsx(wb);
const outputPath=path.join(outDir,stem+'.xlsx');await file.save(outputPath);
const manifest={schema_version:'project_report_v1',generated_at_utc:new Date().toISOString(),output:path.relative(root,outputPath).replaceAll('\\','/'),output_sha256:sha(await fs.readFile(outputPath)),inputs_sha256:data.fingerprint,git_revision_at_generation:data.git,runtime:{node:process.version,artifact_tool:artifactVersion},counts:{tasks:tasks.length,completed_tasks:done,sources:sources.length,feasibility_rows:data.feasibility.length,source_detail_rows:details.length,documentation_rows:documentation.length},input_files:data.inputs,previews:rendered,formula_dependency_test:'PASS',research_validation_as_of:data.validation.checked_at_utc};
await fs.writeFile(path.join(outDir,stem+'.manifest.json'),JSON.stringify(manifest,null,2)+'\n');
console.log('XLSX:',outputPath);
