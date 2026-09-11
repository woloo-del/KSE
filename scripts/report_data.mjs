import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';

export const STATUS = {'Not Started':'Do zrobienia','In Progress':'W toku','At Risk':'Zagrożone','Complete':'Zrobione'};
export const DOCUMENTS = [
  'README.md','docs/01_data_research.md','docs/02_feasibility_matrix.md',
  'docs/03_system_architecture.md','docs/04_data_model.md','docs/05_grid_capacity_methodology.md',
  'docs/06_scoring_methodology.md','docs/07_data_quality.md','docs/08_roadmap.md',
  'docs/gpz_pipeline.md','docs/decision_log.md','docs/discovery_log.md',
  'docs/reproducibility.md','docs/git_workflow.md','docs/project_reporting.md',
  'docs/09_pilot_scope.md',
  'docs/10_radkowice_pilot.md',
];
export const sha = b => crypto.createHash('sha256').update(b).digest('hex');
export const plain = s => String(s ?? '').replace(/\[([^\]]+)\]\(([^)]+)\)/g,'$1 ($2)').replace(/\*\*|`/g,'');

export function validateTasks(data) {
  if (data.schema_version !== 'todo_v1' || !Array.isArray(data.tasks) || !data.tasks.length) throw Error('Niepoprawny rejestr TODO');
  const byId = new Map(data.tasks.map(t=>[t.id,t]));
  if (byId.size !== data.tasks.length) throw Error('Powtórzone ID zadania');
  for (const t of data.tasks) {
    if (!/^KSE-\d{3,}$/.test(t.id) || !t.title || !t.acceptance || !t.next_action || !t.stage || !t.owner) throw Error(`Niepełne zadanie ${t.id}`);
    if (!Object.hasOwn(STATUS,t.status) || !['P0','P1','P2'].includes(t.priority) || !Array.isArray(t.depends_on)) throw Error(`Niepoprawny status/priorytet ${t.id}`);
    for (const d of t.depends_on) if (!byId.has(d)) throw Error(`Nieznana zależność ${t.id}: ${d}`);
    for (const key of ['started_at','completed_at','due_date']) if (t[key] && (!/^\d{4}-\d{2}-\d{2}$/.test(t[key]) || new Date(t[key]).toISOString().slice(0,10)!==t[key])) throw Error(`Niepoprawna data ${t.id}`);
    if (t.status === 'Complete' && (!t.completed_at || !t.evidence?.length)) throw Error(`Brak dowodu zakończenia ${t.id}`);
    if (t.status !== 'Complete' && t.completed_at) throw Error(`Sprzeczny status zakończenia ${t.id}`);
    if (t.started_at && t.completed_at && t.started_at>t.completed_at) throw Error(`Odwrócone daty ${t.id}`);
    if (t.status === 'Complete' && t.depends_on.some(d=>byId.get(d).status!=='Complete')) throw Error(`Nieukończona zależność zamkniętego zadania ${t.id}`);
  }
  const visiting=new Set(), visited=new Set();
  function visit(id) {
    if(visiting.has(id)) throw Error(`Cykl zależności ${id}`);
    if(visited.has(id)) return;
    visiting.add(id); byId.get(id).depends_on.forEach(visit); visiting.delete(id); visited.add(id);
  }
  data.tasks.forEach(t=>visit(t.id));
  return data.tasks.map(t=>({...t,unmet_dependencies:t.depends_on.filter(id=>byId.get(id).status!=='Complete')}));
}

export function parseFeasibility(text) {
  const rows=text.split(/\r?\n/).filter(l=>l.startsWith('|')).map(l=>l.slice(1,-1).split('|').map(x=>plain(x.trim())));
  const valid=new Set(['AVAILABLE_DIRECTLY','CALCULABLE','ESTIMABLE','NOT_CURRENTLY_AVAILABLE']);
  const result=rows.slice(2);
  if(!result.length || result.some(r=>r.length!==4 || !valid.has(r[1]))) throw Error('Zmieniony schemat macierzy wykonalności');
  return result;
}

export function documentRows(relative,text) {
  let heading='', buffer=[], rows=[];
  function flush(){
    if(!buffer.length) return;
    const words=plain(buffer.join(' ')).split(/\s+/); let chunk='';
    for(const word of words){
      if(chunk.length+word.length>650 && chunk){rows.push([relative,heading,chunk]);chunk='';}
      chunk+=(chunk?' ':'')+word;
    }
    if(chunk) rows.push([relative,heading,chunk]); buffer=[];
  }
  for(const line of text.split(/\r?\n/)) {
    if(/^#{1,6} /.test(line)){flush();heading=plain(line.replace(/^#+ /,''));}
    else if(!line.trim()){flush();}
    else if(/^\|[-: |]+\|$/.test(line)||line.startsWith('```')){flush();}
    else if(line.startsWith('|')){flush();buffer.push(line.slice(1,-1).split('|').map(x=>x.trim()).join(' / '));flush();}
    else buffer.push(line);
  }
  flush(); return rows;
}

export async function collect(root) {
  const inputs=[];
  async function read(relative) {
    // Allowlisted files only: never traverse the workspace or load credentials.
    if(relative.split(/[\\/]/).includes('_secrets')) throw Error('Zabronione źródło raportu');
    const b=await fs.readFile(path.join(root,relative)); inputs.push({path:relative,sha256:sha(b),bytes:b.length});
    return b.toString('utf8').replace(/^\uFEFF/,'');
  }
  const todo=JSON.parse(await read('data/project/todo.json'));
  const tasks=validateTasks(todo);
  for(const t of tasks) for(const e of t.evidence??[]) {
    const p=path.resolve(root,e); if(!p.startsWith(root+path.sep) || e.split(/[\\/]/).includes('_secrets')) throw Error(`Niedozwolony dowód ${t.id}`);
    await fs.access(p);
  }
  const catalog=JSON.parse(await read('data/catalog/data_sources.json'));
  if(!catalog.sources?.length || new Set(catalog.sources.map(s=>s.source_id)).size!==catalog.sources.length) throw Error('Niepoprawny katalog źródeł');
  const validation=JSON.parse(await read('data/catalog/research_validation.json'));
  const archive=JSON.parse(await read('data/catalog/archive_manifest.json'));
  const docs={}; for(const name of DOCUMENTS) docs[name]=await read(name);
  let git='UNKNOWN'; try {git=execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8',stdio:['ignore','pipe','ignore']}).trim();}catch{}
  const fingerprint=sha(JSON.stringify(inputs));
  return {todo,tasks,catalog,validation,archive,docs,inputs,fingerprint,git,feasibility:parseFeasibility(docs['docs/02_feasibility_matrix.md'])};
}

export function todoMarkdown(data) {
  const tasks=data.tasks;
  const lines=['# TODO — Grid Connection Intelligence','',`Aktualizacja rejestru: **${data.todo.updated_at}**. Źródło edytowalne: [todo.json](data/project/todo.json).`,
    '', 'Widok generowany. Aktualizujemy JSON, zachowując ID, historię Git i dowody zakończenia. Nie ustalono terminów dla niezaplanowanych zadań. P0 = warunek najbliższego etapu, P1 = rozwój po fundamentach, P2 = dalszy rozwój. Priorytety są kolejnością organizacji pracy, nie scoringiem sieci.',
    '', '## Najbliższe zadania bez nieukończonych zależności',''];
  for(const t of tasks.filter(t=>t.status!=='Complete'&&!t.unmet_dependencies.length).sort((a,b)=>a.priority.localeCompare(b.priority)||a.id.localeCompare(b.id))) lines.push(`- **${t.id} — ${t.title}** (${t.priority}, ${STATUS[t.status]}). ${t.next_action}`);
  lines.push('','## Pełny rejestr','','| ID | Zadanie | Etap | Status | Priorytet | Zależności |','|---|---|---|---|---|---|');
  for(const t of tasks) lines.push(`| ${t.id} | ${t.title} | ${t.stage} | ${STATUS[t.status]} | ${t.priority} | ${t.depends_on.join(', ')||'—'} |`);
  lines.push('','## Kryteria zakończenia i dowody','');
  for(const t of tasks) lines.push(`### ${t.id} — ${t.title}`,'',`- Odpowiedzialność: ${t.owner}.`,`- Następny krok: ${t.next_action}`,`- Kryterium: ${t.acceptance}`,`- Nieukończone zależności: ${t.unmet_dependencies.join(', ')||'brak'}.`,`- Ryzyko: ${t.risk||'brak dodatkowej uwagi w rejestrze'}.`,`- Termin docelowy: ${t.due_date||'nie ustalono'}.`,`- Zakończono: ${t.completed_at||'nie zakończono'}.`,`- Dowody/kontekst: ${(t.evidence??[]).map(e=>`[${e}](${e})`).join(', ')}.`,'');
  return lines.join('\n').trimEnd()+'\n';
}
