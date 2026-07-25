#!/usr/bin/env python3
"""Validate a PêcheScore release manifest and local assets without dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
FORBIDDEN_SUFFIXES = (".nc", ".nc.xz", ".xz", ".pyc")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--assets-dir", type=Path)
    args = parser.parse_args()

    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    assets = data.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append("assets must be a non-empty list")
        assets = []

    seen_ids: set[str] = set()
    seen_names: set[str] = set()
    for index, asset in enumerate(assets):
        prefix = f"assets[{index}]"
        asset_id = asset.get("id")
        name = asset.get("fileName")
        checksum = asset.get("sha256")
        url = asset.get("downloadUrl")
        size = asset.get("sizeBytes")

        if not isinstance(asset_id, str) or not asset_id:
            errors.append(f"{prefix}.id missing")
        elif asset_id in seen_ids:
            errors.append(f"duplicate id: {asset_id}")
        else:
            seen_ids.add(asset_id)

        if not isinstance(name, str) or not name:
            errors.append(f"{prefix}.fileName missing")
            continue
        if name in seen_names:
            errors.append(f"duplicate fileName: {name}")
        seen_names.add(name)
        if name.lower().endswith(FORBIDDEN_SUFFIXES):
            errors.append(f"forbidden asset type: {name}")

        if not isinstance(checksum, str) or not SHA256_RE.fullmatch(checksum):
            errors.append(f"{prefix}.sha256 invalid")
        if not isinstance(size, int) or size <= 0:
            errors.append(f"{prefix}.sizeBytes invalid")
        if not isinstance(url, str) or urlparse(url).scheme != "https":
            errors.append(f"{prefix}.downloadUrl must be HTTPS")

        if args.assets_dir:
            path = args.assets_dir / name
            if not path.is_file():
                errors.append(f"missing local asset: {path}")
            else:
                if path.stat().st_size != size:
                    errors.append(f"size mismatch: {name}")
                if SHA256_RE.fullmatch(checksum or "") and sha256(path) != checksum:
                    errors.append(f"SHA-256 mismatch: {name}")

    if errors:
        print("MANIFEST INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"MANIFEST VALID: {len(assets)} asset(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
