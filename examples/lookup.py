#!/usr/bin/env python3
"""
Simple CLI lookup tool for the RouterIPHub open database.
Usage:
  python lookup.py <brand, model, or IP>
  python lookup.py --ip 192.168.50.1
  python lookup.py --brand Netgear
"""
import argparse
import json
import os
import sys


def load_routers():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'routers.json')
    if not os.path.exists(data_path):
        print(f"Error: data file not found at {data_path}", file=sys.stderr)
        sys.exit(1)

    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def filter_routers(routers, query=None, ip=None, brand=None, model=None):
    matches = routers
    if query:
        q = query.lower()
        matches = [
            r for r in matches
            if q in r.get('brand', '').lower()
            or q in r.get('model_name', '').lower()
            or q == r.get('default_ip', '').lower()
        ]
    if ip:
        matches = [r for r in matches if r.get('default_ip') == ip]
    if brand:
        b = brand.lower()
        matches = [r for r in matches if b in r.get('brand', '').lower()]
    if model:
        m = model.lower()
        matches = [r for r in matches if m in r.get('model_name', '').lower()]
    return matches


def print_results(matches, label):
    if not matches:
        print(f"No models found matching: '{label}'")
        return

    print(f"\nFound {len(matches)} matching model(s) for '{label}':\n" + "=" * 60)
    for r in matches[:20]:
        slug = r.get('slug', '')
        web_sheet = f"https://routeriphub.com/routers/{slug}/" if slug else "https://routeriphub.com/routers/"
        print(f"[{r.get('brand', 'Unknown')}] {r.get('model_name', 'Unknown')}")
        print(f"  - Gateway IP : {r.get('default_ip', '')}")
        print(f"  - Username   : {r.get('default_username') or '[Leave Blank]'}")
        print(f"  - Password   : {r.get('default_password') or '[Leave Blank]'}")
        print(f"  - Standard   : {r.get('wifi_standard', '')}")
        print(f"  - Web Sheet  : {web_sheet}\n")

    if len(matches) > 20:
        print(f"... and {len(matches) - 20} more models. Refine your query for narrower results.")


def main():
    parser = argparse.ArgumentParser(description="CLI lookup tool for the RouterIPHub router database.")
    parser.add_argument("query", nargs="?", help="Brand, model name, or default gateway IP")
    parser.add_argument("--ip", help="Filter by exact default gateway IP (e.g. 192.168.50.1)")
    parser.add_argument("--brand", help="Filter by brand name (e.g. Netgear)")
    parser.add_argument("--model", help="Filter by model name (e.g. AX55)")
    args = parser.parse_args()

    if not any([args.query, args.ip, args.brand, args.model]):
        parser.print_help()
        print("\nExamples:")
        print("  python examples/lookup.py Netgear")
        print("  python examples/lookup.py --ip 192.168.50.1")
        print("  python examples/lookup.py --brand Netgear")
        print("  python examples/lookup.py AX55")
        sys.exit(1)

    routers = load_routers()
    matches = filter_routers(routers, query=args.query, ip=args.ip, brand=args.brand, model=args.model)
    label = " ".join(p for p in [args.query, args.ip, args.brand, args.model] if p)
    print_results(matches, label)


if __name__ == '__main__':
    main()
