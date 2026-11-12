#!/usr/bin/env bash
# Quick bash/curl one-liner lookup
QUERY="${1:-Netgear}"
echo "Searching for: $QUERY"
curl -s https://raw.githubusercontent.com/routeriphub/default-router-ip-database/main/data/routers.json \
  | jq --arg q "$QUERY" '.[] | select((.brand | ascii_downcase | contains($q | ascii_downcase)) or (.default_ip == $q)) | {brand: .brand, model: .model, ip: .default_ip, password: .default_password}'
