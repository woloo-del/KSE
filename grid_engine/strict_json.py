"""Shared JSON decoding rules for auditable snapshot inputs."""
from decimal import Decimal
import json


def decode_json(raw: bytes) -> object:
    def reject_constant(value: str) -> None:
        raise ValueError('NONFINITE_JSON_NUMBER')

    def unique_fields(pairs: list[tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('DUPLICATE_JSON_FIELD')
            result[key] = value
        return result

    return json.loads(raw.decode('utf-8-sig'), parse_float=Decimal,
                      parse_constant=reject_constant, object_pairs_hook=unique_fields)
