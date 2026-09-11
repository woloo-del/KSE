import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {validateTasks,parseFeasibility,documentRows,todoMarkdown} from '../scripts/report_data.mjs';

const original=JSON.parse(await fs.readFile(new URL('../data/project/todo.json',import.meta.url),'utf8'));
const copy=()=>structuredClone(original);
test('real TODO has stable unique IDs and preserves missing deadlines',()=>{
  const tasks=validateTasks(original);
  assert.equal(tasks.length,original.tasks.length);
  assert.equal(tasks.find(t=>t.id==='KSE-014').unmet_dependencies[0],'KSE-013');
  assert.equal(tasks.find(t=>t.id==='KSE-029').due_date,undefined);
});
test('duplicate IDs and unknown dependencies are rejected',()=>{
  const a=copy();a.tasks.push(a.tasks[0]);assert.throws(()=>validateTasks(a),/Powtórzone/);
  const b=copy();b.tasks.at(-1).depends_on=['KSE-999'];assert.throws(()=>validateTasks(b),/Nieznana zależność/);
});
test('cycles and premature completion are rejected',()=>{
  // Isolated synthetic graph: real task completion must not change this test's premise.
  const task=(id,depends_on)=>({...original.tasks[0],id,title:'SYNTHETIC GRAPH TEST',status:'Not Started',completed_at:undefined,depends_on});
  const a={schema_version:'todo_v1',tasks:[task('KSE-901',['KSE-902']),task('KSE-902',['KSE-901'])]};
  assert.throws(()=>validateTasks(a),/Cykl/);
  const b=structuredClone(a);b.tasks[1].depends_on=[];b.tasks[0].status='Complete';b.tasks[0].completed_at='2026-09-10';
  assert.throws(()=>validateTasks(b),/Nieukończona zależność/);
});
test('completion requires evidence and invalid dates fail',()=>{
  const a=copy();a.tasks[0].evidence=[];assert.throws(()=>validateTasks(a),/Brak dowodu/);
  const b=copy();b.tasks[0].due_date='2026-02-30';assert.throws(()=>validateTasks(b),/Niepoprawna data/);
});
test('real feasibility table preserves every data row',async()=>{
  const text=await fs.readFile(new URL('../docs/02_feasibility_matrix.md',import.meta.url),'utf8');
  assert.equal(parseFeasibility(text).length,text.split(/\r?\n/).filter(l=>l.startsWith('|')).length-2);
  assert.throws(()=>parseFeasibility('| a | b |\n|---|---|\n| x | WRONG |'),/schemat/);
});
test('long explanatory content and source URL are not truncated',()=>{
  const body=Array(500).fill('dowód').join(' ');
  const rows=documentRows('test.md',`# Test\n\n${body}\n\n[Źródło](https://example.org/source)`);
  assert.equal(rows.slice(0,-1).map(r=>r[2]).join(' '),body);
  assert.match(rows.at(-1)[2],/https:\/\/example.org\/source/);
});
test('TODO view scales past the 30-row plan without dropping records',()=>{
  const a=copy();a.tasks.push({...a.tasks.at(-1),id:'KSE-999',title:'SYNTHETIC TEST TASK'});
  const tasks=validateTasks(a);assert.equal(tasks.length,original.tasks.length+1);
  assert.ok(tasks.length>30);
  assert.match(todoMarkdown({todo:a,tasks}),/KSE-999/);
});
