#!/usr/bin/env python3
"""Build Mihomo rule-provider files from the shared Iran Lite preset."""

import argparse
import gzip
import ipaddress
import json
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("preset", type=Path)
    parser.add_argument("mihomo", type=Path)
    args = parser.parse_args()
    rules = json.loads(gzip.decompress(args.preset.read_bytes()))
    if [(rule["outboundTag"], rule["enabled"]) for rule in rules] != [
        ("direct", True), ("direct", True), ("proxy", True),
    ]:
        raise ValueError("The preset has an unexpected rule order or policy.")
    domains, cidrs = rules[0]["domain"], rules[1]["ip"]
    if any(not entry.startswith("domain:") or not entry[7:] for entry in domains):
        raise ValueError("This converter supports the preset's domain suffix matchers only.")
    sets = {
        "iran-domains": ("domain", [f"+.{entry[7:]}" for entry in domains]),
        "iran-ips": ("ipcidr", [str(ipaddress.ip_network(entry)) for entry in cidrs]),
    }
    output = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as work:
        source = Path(work) / "rules.txt"
        for name, (behavior, entries) in sets.items():
            source.write_text("\n".join(entries) + "\n", encoding="utf-8")
            subprocess.run(
                [str(args.mihomo.resolve()), "convert-ruleset", behavior, "text", str(source), str(output / f"{name}.mrs")],
                check=True,
            )
            print(f"{name}: {len(entries)} source matchers")


if __name__ == "__main__":
    main()
