"""Build explicit research catalog and Markdown view from editorial source notes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def build_catalog() -> dict[str, Any]:
    notes = json.loads((ROOT / "data/catalog/source_notes.json").read_text(encoding="utf-8"))
    checked = notes["verification_date"]
    pilot_notes = ROOT / "data/catalog/radkowice_source_notes.json"
    if pilot_notes.exists():
        notes['sources'].extend(json.loads(pilot_notes.read_text(encoding='utf-8'))['sources'])
    manifests = []
    paths = sorted((ROOT / "data/catalog").glob("probe_results_*.json"))
    pilot_manifest = ROOT / "data/catalog/radkowice_snapshot_manifest.json"
    if pilot_manifest.exists():
        paths.append(pilot_manifest)
    for path in paths:
        for probe in json.loads(path.read_text(encoding="utf-8-sig")):
            manifests.append({**probe, "manifest": path.relative_to(ROOT).as_posix()})
    result = []
    for note in notes["sources"]:
        row: dict[str, Any] = {
            "country": "PL",
            "geographical_scope": "Zakres publikacji danego operatora/instytucji; nie założono pełnego pokrycia kraju.",
            "grid_voltage": ["UNKNOWN_OR_NOT_APPLICABLE"],
            "api_available": "UNKNOWN",
            "gis_available": "UNKNOWN",
            "update_frequency": "UNKNOWN — nie ustalono gwarantowanego cyklu publikacji.",
            "historical_data": "UNKNOWN — własne snapshoty od 10.09.2026, jeśli zapisano próbkę.",
            "authentication": "Odczyt publicznej strony bez konta; nie dowodzi dostępu do wszystkich danych.",
            "license": "UNKNOWN — nie potwierdzono otwartej licencji wybranego zbioru.",
            "license_url": None,
            "commercial_use": "UNKNOWN",
            "machine_readable": "UNKNOWN",
            "scraping_required": "UNKNOWN — przed scraperem preferować oficjalny plik lub API.",
            "data_quality_score": None,
            "quality_score_status": "NOT_CALIBRATED — autorytet źródła nie jest procentem kompletności lub trafności.",
            "last_verified": checked,
            "last_successful_verification": checked,
            "source_date": None,
            "publication_date": None,
            "source_version": None,
            "source_page": None,
            "valid_from": None,
            "valid_to": None,
            "current_future_scope": "SOURCE_DEPENDENT",
            "value_classification_default": "REPORTED",
            "automation_notes": "Jednorazowy przegląd; brak zgody na stały scraper wynikającej z samego dostępu. Sprawdzić warunki, robots.txt i limity przed wdrożeniem.",
            "probe_ids": [],
            "related_urls": [],
        }
        row.update(note)
        if row["verification_status"] in {"DISCOVERED", "BLOCKED"}:
            row["last_successful_verification"] = None
            row["authentication"] = note.get("authentication", "UNKNOWN — pełna treść nie została zweryfikowana.")
        row["evidence"] = [probe for probe in manifests if probe["source_id"] in row["probe_ids"]]
        row["retrieval_date"] = [probe["retrieval_date"] for probe in row["evidence"]]
        result.append(row)
    return {
        "schema_version": notes["schema_version"],
        "as_of": max(row['last_verified'] for row in result),
        "scope": "STAGE_1_RESEARCH_ONLY",
        "source_of_truth": "data/catalog/source_notes.json + data/catalog/radkowice_source_notes.json when present; this file is generated",
        "classification_note": "REPORTED indicates attributed publication, not automatic truth or MEASURED telemetry. Community and model data remain separately classified.",
        "sources": result,
    }


def markdown(catalog: dict[str, Any]) -> str:
    lines = [
        "# Rejestr źródeł danych",
        "",
        f"Stan badania: **{catalog['as_of']}**. Źródła: **{len(catalog['sources'])}**.",
        "",
        "Widok generowany z `data/catalog/source_notes.json`. Pełne pola i manifesty: `data/catalog/data_sources.json`. Raport: [01_data_research.md](01_data_research.md).",
        "",
        "`SAMPLE_VERIFIED` oznacza odczytaną próbkę, nie walidację całego zbioru; `CONTENT_REVIEWED` — treść strony/dokumentu; `DOCUMENTATION_REVIEWED` — opis interfejsu; `DISCOVERED` — tylko wskazanie; `BLOCKED` — nieudany odczyt. GetCapabilities nie jest testem GetFeature. `UNKNOWN` oznacza brak rozstrzygnięcia, nie brak interfejsu.",
        "",
        "A–H opisuje autorytet/proweniencję według AGENTS.md; dla bibliotek i modeli H nie jest oceną jakości oprogramowania. `data_quality_score=null` dla wszystkich źródeł: nie skalibrowano liczbowej miary jakości. Daty źródłowe pozostają puste, jeśli nie zostały rozstrzygnięte.",
        "",
        "| ID | Źródło | Weryfikacja | Priorytet | Użycie komercyjne |",
        "|---|---|---|---|---|",
    ]
    for row in catalog["sources"]:
        name = row["source_name"].replace("|", "/")
        lines.append(f"| {row['source_id']} | [{name}]({row['url']}) | {row['verification_status']} | {row['priority']} | {row['commercial_use']} |")
    lines += ["", "## Karty źródeł", ""]
    fields = [
        ("operator", "Operator"), ("data_owner", "Właściciel"),
        ("country", "Kraj"), ("data_category", "Kategoria"),
        ("grid_voltage", "Napięcie"), ("geographical_scope", "Zasięg"),
        ("data_format", "Format"), ("api_available", "API"),
        ("gis_available", "GIS"), ("update_frequency", "Aktualizacja"),
        ("historical_data", "Historia"), ("authentication", "Uwierzytelnienie"),
        ("license", "Licencja"), ("commercial_use", "Użycie komercyjne"),
        ("reliability", "Autorytet źródła"), ("machine_readable", "Odczyt maszynowy"),
        ("scraping_required", "Scraping"), ("key_fields", "Pola"),
        ("potential_application", "Zastosowanie"), ("known_limitations", "Ograniczenia"),
        ("source_date", "Data stanu źródła"), ("publication_date", "Publikacja"),
        ("source_version", "Wersja"), ("source_page", "Strona źródła"),
        ("last_verified", "Sprawdzono"), ("last_successful_verification", "Udany odczyt"),
        ("value_classification_default", "Klasyfikacja wejścia"),
        ("automation_notes", "Automatyzacja"),
    ]
    for row in catalog["sources"]:
        lines += [f"### {row['source_id']} — {row['source_name']}", "", f"[Źródło]({row['url']})", ""]
        for key, label in fields:
            value = row[key]
            if isinstance(value, list):
                value = "; ".join(value)
            lines.append(f"- **{label}:** {value if value is not None else 'UNKNOWN / nie dotyczy'}")
        if row.get("date_conflict"):
            lines.append(f"- **Konflikt dat:** `{json.dumps(row['date_conflict'], ensure_ascii=False)}`")
        if row.get("date_notes"):
            lines.append(f"- **Daty — uwagi:** {row['date_notes']}")
        if row["license_url"]:
            lines.append(f"- **Warunki:** [źródło prawne]({row['license_url']})")
        for url in row["related_urls"]:
            lines.append(f"- **Powiązane źródło/interfejs:** [link]({url})")
        for evidence in row["evidence"]:
            lines.append(f"- **Próba {evidence['source_id']}:** HTTP {evidence['http_status']}; {evidence['retrieval_date']}; `{evidence['manifest']}`; próbka `{evidence['local_path']}`.")
        lines += ["", "Ocena liczbowa jakości: **nie ustalono**. Dostępność techniczna nie jest zgodą na ponowne wykorzystanie.", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    output = build_catalog()
    (ROOT / "data/catalog/data_sources.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "docs/data_sources.md").write_text(markdown(output).rstrip() + "\n", encoding="utf-8")
    print(f"Built {len(output['sources'])} source records and Markdown view.")
