#!/bin/bash

# Path to your Squid log
LOG_FILE="/var/log/squid/access.log"

# API endpoint
API_URL="http://localhost:8080/add_url/"

# Content type header
CONTENT_TYPE="Content-Type: application/json"

echo "[INFO] Monitoring $LOG_FILE for CONNECT requests..."

tail -F "$LOG_FILE" | \
grep --line-buffered 'CONNECT' | \
sed -un 's/.*CONNECT \([^:"]*\):.*/\1/p' | \
while IFS= read -r domain; do
    if [[ -n "$domain" ]]; then
        url="https://$domain"
        echo "[INFO] Sending: $url"
        curl -s -X POST "$API_URL" -H "$CONTENT_TYPE" -d "{\"url\": \"$url\"}"
    fi
done

