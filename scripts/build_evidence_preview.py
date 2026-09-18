"""Generate an inline concept from explicit public snapshots, without network access."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from backend.profile_browser import browser_data


def build(output: Path) -> None:
    data = browser_data()
    template = (ROOT / 'docs/prototypes/evidence-workspace.template.html').read_text(encoding='utf-8')
    assert template.count('__KSE_DATA__') == 1
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.replace('__KSE_DATA__', payload), encoding='utf-8', newline='\n')
    print(f'{len(data["profiles"])} profiles; {output.stat().st_size} bytes')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    build(parser.parse_args().output)
