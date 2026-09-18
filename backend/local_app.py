"""Read-only local pilot. Only named public snapshots and static assets are served."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from grid_engine.screening_opinion import assess
from grid_engine.evidence_links import link_records, review_queue
from backend.profile_browser import browser_data

INPUTS = {
    'pipeline': 'data/reference/radkowice_pipeline_view_2026-07-31_v1.json',
    'graph': 'data/reference/radkowice_evidence_graph_v2.json',
    'requests': 'data/project/information_requests.json',
    'catalog': 'data/catalog/data_sources.json',
    'investment_review': 'data/reference/radkowice_investment_dates_2026-09-17_v1.json',
    'investment_stages': 'data/reference/radkowice_portal_stages_2026-09-18_v1.json',
    'development_plan': 'data/reference/radkowice_development_plan_2026-04_v1.json',
    'aggregated_evidence': 'data/reference/radkowice_aggregated_evidence_2026-09-17_v1.json',
}
ASSETS = {'/': ('index.html', 'text/html; charset=utf-8'),
          '/profiles': ('profiles.html', 'text/html; charset=utf-8'),
          '/profiles.js': ('profiles.js', 'text/javascript; charset=utf-8'),
          '/profiles.css': ('profiles.css', 'text/css; charset=utf-8'),
          '/app.js': ('app.js', 'text/javascript; charset=utf-8'),
          '/style.css': ('style.css', 'text/css; charset=utf-8')}


def snapshot() -> dict:
    loaded, hashes = {}, {}
    for key, name in INPUTS.items():
        raw = (ROOT / name).read_bytes()
        loaded[key] = json.loads(raw)
        hashes[name] = hashlib.sha256(raw).hexdigest()
    ids = {e['source_id'] for node in loaded['graph']['entities'] for e in node['evidence']}
    ids.update({'PSE_PIPELINE', 'PSE_RADK_BRIDGE_NOTICE_2025', 'RDOS_RADK_PIASKI_DECISION_2025',
                'PGE_EXPORT_DISCOVERY', 'PGE_PLAN_DISCOVERY', 'PSE_INVESTMENTS_RADK', 'PSE_IMPACT_REPORT_2023',
                'PSE_PRSP_2027_2036_POST_CONSULTATION', 'PSE_RADK_STAGES', 'OSM_RADK_STATION_AREA'})
    fields = ('source_id', 'source_name', 'url', 'last_verified', 'source_date',
              'verification_status', 'known_limitations', 'license', 'commercial_use')
    sources = [{key: source.get(key) for key in fields} for source in loaded['catalog']['sources'] if source['source_id'] in ids]
    links = link_records(loaded['aggregated_evidence'], loaded['graph'])
    return {'station': 'SE Radkowice', 'pipeline': loaded['pipeline'],
            'graph': loaded['graph'], 'requests': loaded['requests']['items'],
            'sources': sources, 'catalog_date': loaded['catalog']['as_of'],
            'investment_review': loaded['investment_review'],
            'development_plan': loaded['development_plan'],
            'investment_stages': loaded['investment_stages'],
            'aggregated_evidence': loaded['aggregated_evidence'],
            'evidence_links': links,
            'evidence_review_queue': review_queue(links, loaded['requests']['items']),
            'input_sha256': hashes, 'scope': 'Lokalny pilot dokumentacyjny; dane publiczne, aktualizowane ręcznie.'}


class Handler(BaseHTTPRequestHandler):
    def reply(self, code: int, data: bytes, content_type: str) -> None:
        self.send_response(code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def json_reply(self, code: int, value: dict) -> None:
        self.reply(code, json.dumps(value, ensure_ascii=False, allow_nan=False).encode(), 'application/json; charset=utf-8')

    def do_GET(self) -> None:
        route = urlsplit(self.path).path
        try:
            if route == '/api/station':
                self.json_reply(200, snapshot())
            elif route == '/api/profiles':
                self.json_reply(200, browser_data())
            elif route in ASSETS:
                name, kind = ASSETS[route]
                self.reply(200, (ROOT / 'frontend' / name).read_bytes(), kind)
            else:
                self.json_reply(404, {'error': 'Nie znaleziono zasobu.'})
        except (OSError, ValueError, KeyError):
            self.json_reply(503, {'error': 'Nie można odczytać danych pilota. Sprawdź pliki wejściowe.'})

    def do_POST(self) -> None:
        if self.path != '/api/assessment':
            self.json_reply(404, {'error': 'Nie znaleziono zasobu.'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 16384:
                raise ValueError('Nieprawidłowy rozmiar żądania.')
            project = json.loads(self.rfile.read(length))
            if not isinstance(project, dict):
                raise ValueError('Wymagany obiekt parametrów projektu.')
            data = snapshot()
            result = assess(project, data['pipeline'], data['investment_review'])
            result['input_sha256'] = data['input_sha256']
            result['evaluated_at'] = datetime.now(timezone.utc).isoformat()
            result['evidence_snapshot'] = data
            result['method_code_sha256'] = hashlib.sha256((ROOT / 'grid_engine/screening_opinion.py').read_bytes()).hexdigest()
            self.json_reply(200, result)
        except (ValueError, KeyError):
            self.json_reply(400, {'error': 'Sprawdź technologię, napięcie i nieujemne wartości liczbowe.'})
        except OSError:
            self.json_reply(503, {'error': 'Dane pilota są niedostępne.'})

    def log_message(self, *args) -> None:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8787)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(f'KSE pilot: http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
