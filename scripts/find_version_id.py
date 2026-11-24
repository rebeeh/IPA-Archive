#!/usr/bin/env python3
"""
find_version_id.py
Helper utility to resolve externalVersionID from ipatool list-versions output,
or to verify a specific externalVersionID against the App Store metadata API.
"""

import argparse
import json
import subprocess
import sys


def get_version_metadata(ipatool_path: str, bundle_id: str, version_id: str):
    cmd = [
        ipatool_path,
        "get-version-metadata",
        "-b",
        bundle_id,
        "--external-version-id",
        version_id,
        "--format",
        "json",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Verify or scan iOS App Store externalVersionIDs using ipatool."
    )
    parser.add_argument(
        "-b", "--bundle-id", required=True, help="Application bundle ID (e.g. com.toyopagroup.picaboo)"
    )
    parser.add_argument(
        "--id", help="Single external version ID to verify (e.g. from ipafilezone.st)"
    )
    parser.add_argument(
        "--ipatool", default="ipatool", help="Path to ipatool binary (default: 'ipatool')"
    )

    args = parser.parse_args()

    if args.id:
        print(f"[*] Querying metadata for bundle: {args.bundle_id}, version ID: {args.id}...")
        meta = get_version_metadata(args.ipatool, args.bundle_id, args.id)
        if meta and meta.get("success"):
            print(f"[+] Found Match:")
            print(f"    Display Version: {meta.get('displayVersion')}")
            print(f"    External ID:     {meta.get('externalVersionID')}")
            print(f"    Release Date:    {meta.get('releaseDate')}")
        else:
            print("[-] Failed to retrieve metadata. Check bundle ID and version ID.")
            sys.exit(1)


if __name__ == "__main__":
    main()
