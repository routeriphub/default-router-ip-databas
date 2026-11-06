#!/usr/bin/env python3
"""
Simple CLI lookup tool for the RouterIPHub open database.
Usage: python lookup.py <brand, model, or IP>
"""
import json
import sys
import os

def search(query):
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'routers.json')
    if not os.path.exists(data_path):
        print(f"Error: data file not found at {data_path}")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        routers = json.load(f)

    q = query.lower()
    matches = [
        r for r in routers 
        if q in r['brand'].lower() or q in r['model'].lower() or q == r['default_ip']
    ]

    if not matches:
        print(f"No models found matching: '{query}'")
        return

    print(f"\nFound {len(matches)} matching model(s) for '{query}':\n" + "="*60)
    for r in matches[:20]:
        print(f"[{r['brand']}] {r['model']}")
        print(f"  • Gateway IP : {r['default_ip']}")
        print(f"  • Username   : {r['default_username']}")
        print(f"  • Password   : {r['default_password'] or '[Leave Blank]'}")
        print(f"  • Standard   : {r['wifi_standard']}")
        print(f"  • Web Sheet  : {r['web_profile']}\n")

    if len(matches) > 20:
        print(f"... and {len(matches) - 20} more models. Refine your query for narrower results.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python lookup.py <brand, model, or IP>")
        print("Examples:")
        print("  python lookup.py Netgear")
        print("  python lookup.py 192.168.2.1")
        print("  python lookup.py AX55")
        sys.exit(1)
    search(sys.argv[1])
