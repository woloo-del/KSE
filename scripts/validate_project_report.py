"""Read-only verification of exported report values, provenance and template formulas."""
import hashlib
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

import openpyxl


def validate(report: Path) -> dict:
    root = Path(__file__).resolve().parents[1]
    tasks = json.loads((root / 'data/project/todo.json').read_text(encoding='utf-8'))['tasks']
    sources = json.loads((root / 'data/catalog/data_sources.json').read_text(encoding='utf-8'))['sources']
    manifest = json.loads(report.with_suffix('.manifest.json').read_text(encoding='utf-8'))
    values = openpyxl.load_workbook(report, data_only=True)
    formulas = openpyxl.load_workbook(report, data_only=False)
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    check('Ten report sheets', len(values.sheetnames) == 10)
    check('All task IDs', {values['TODO'].cell(r, 1).value for r in range(7, len(tasks)+7)} == {t['id'] for t in tasks})
    check('All source IDs', {values['Źródła'].cell(r, 1).value for r in range(7, len(sources)+7)} == {s['source_id'] for s in sources})
    for i, task in enumerate(tasks, 7):
        check(f"Deadline {task['id']}", values['TODO'].cell(i, 12).value is None if not task.get('due_date') else values['TODO'].cell(i, 12).value.date().isoformat() == task['due_date'])
    plan = values['Project Plan']
    start = plan['K9'].value
    check('Timeline dates', all(plan.cell(9, 11+i).value == start+timedelta(days=7*i) for i in range(20)))
    for r in range(10, 40):
        begin, end = plan.cell(r, 7).value, plan.cell(r, 8).value
        expected = (end-begin).days+1 if begin and end and end >= begin else None
        check(f'Duration row {r}', plan.cell(r, 9).value in (None, '') if expected is None else plan.cell(r, 9).value == expected)
        for c in range(11, 31):
            week = plan.cell(9, c).value
            active = expected is not None and week <= end and week+timedelta(days=6) >= begin
            check(f'Gantt {r}:{c}', plan.cell(r, c).value == 1 if active else plan.cell(r, c).value in (None, ''))
    check('Source count formula cache', values['Podsumowanie']['B7'].value == len(sources))
    check('Task count formula cache', values['Podsumowanie']['B8'].value == len(tasks))
    check('Complete count formula cache', values['Podsumowanie']['B9'].value == sum(t['status'] == 'Complete' for t in tasks))
    check('Dates typed', isinstance(values['Audyt']['C7'].value, datetime) and isinstance(values['Odtwarzanie']['B7'].value, datetime))
    check('Native duration formula', formulas['Project Plan']['I11'].data_type == 'f')
    reference = openpyxl.load_workbook(root / 'data/reference/project_tracker_template.xlsx')
    check('Template merges retained', set(map(str, reference['Project Plan'].merged_cells.ranges)) <= set(map(str, formulas['Project Plan'].merged_cells.ranges)))
    check('Template conditional formats retained', len(formulas['Project Plan'].conditional_formatting) >= len(reference['Project Plan'].conditional_formatting))
    check('No Excel errors', not any(c.data_type == 'e' for s in values for row in s for c in row))
    check('Workbook hash', hashlib.sha256(report.read_bytes()).hexdigest() == manifest['output_sha256'])
    check('No secret inputs', not any('_secrets' in i['path'].split('/') for i in manifest['input_files']))
    for item in manifest['input_files']:
        check('Input hash '+item['path'], hashlib.sha256((root/item['path']).read_bytes()).hexdigest() == item['sha256'])
    result = {'status': 'PASS', 'check_count': len(checks), 'checks': checks}
    report.with_suffix('.validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    result = validate(Path(sys.argv[1]).resolve())
    print(f"PASS: {result['check_count']} report checks")
