#!/usr/bin/env python3
"""
sync_locales.py - Sync locales.source.json and _locales/*/messages.json from manifest.json

Generates translation keys for VideoSort extension options following the convention:
  - {option_name}_desc  (lowercase) for each option's description
  - about, description, requirements  for extension-level fields
  - No displayName keys (not translatable)

Usage:
  python3 scripts/sync_locales.py

Modes:
  - Fresh run: generates locales.source.json with English messages
  - Merge run: syncs _locales/*/messages.json, preserving existing translations,
    adding new keys, dropping obsolete ones
"""

import json
import glob
import os
import sys
from collections import OrderedDict


def to_str(val):
    if isinstance(val, list):
        return "\n".join(val)
    return str(val)


def load_manifest(path="manifest.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_source(manifest):
    result = OrderedDict()

    result["about"] = {
        "message": to_str(manifest.get("about", "")),
        "description": "Short description shown in the extension manager table",
    }
    result["description"] = {
        "message": to_str(manifest.get("description", "")),
        "description": "Full description of the extension shown in settings",
    }
    result["requirements"] = {
        "message": to_str(manifest.get("requirements", "")),
        "description": "System requirements displayed to the user",
    }

    for opt in manifest.get("options", []):
        key = opt["name"].lower() + "_desc"
        desc = to_str(opt.get("description", ""))
        result[key] = {
            "message": desc,
            "description": f"Help text for the {opt['name']} option",
        }

    return result


def generate_locale(source_data, existing_data):
    result = OrderedDict()
    for key, entry in source_data.items():
        if key in existing_data and "message" in existing_data[key]:
            result[key] = {
                "message": existing_data[key]["message"],
                "description": entry["description"],
            }
        else:
            result[key] = {
                "message": entry["message"],
                "description": entry["description"],
            }
    return result


def count_changes(source_keys, existing_keys):
    new_keys = source_keys - existing_keys
    removed = existing_keys - source_keys
    return new_keys, removed


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")


def main():
    manifest = load_manifest()
    source_data = generate_source(manifest)
    source_keys = set(source_data.keys())

    total_added = 0
    total_removed = 0

    write_json("locales.source.json", source_data)
    print(f"locales.source.json: {len(source_data)} keys")

    for path in sorted(glob.glob("_locales/*/messages.json")):
        with open(path, "r", encoding="utf-8") as f:
            existing = json.load(f)

        new_keys, removed = count_changes(source_keys, set(existing.keys()))
        locale = generate_locale(source_data, existing)
        write_json(path, locale)

        lang = path.split("/")[1]
        parts = []
        if new_keys:
            parts.append(f"+{len(new_keys)} new")
        if removed:
            parts.append(f"-{len(removed)} removed")
        if parts:
            print(f"  {lang}: {', '.join(parts)}")
        total_added += len(new_keys)
        total_removed += len(removed)

    if total_added or total_removed:
        print(f"Total: +{total_added} added, -{total_removed} removed across all locales")
    else:
        print("All locale files up to date")


if __name__ == "__main__":
    main()
