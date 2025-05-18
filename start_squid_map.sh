#!/bin/bash

# Path to your Squid log
LOG_FILE="/var/log/squid/access.log"

# API endpoint
API_URL="http://localhost:8080/add_url/"

# Content type header
CONTENT_TYPE="Content-Type: application/json"

echo "[INFO] Monitoring $LOG_FILE for CONNECT requests..."

tail -F "$LOG_FILE" | while IFS= read -r line; do
    # Extract source IP (first field)
    src=$(echo "$line" | awk '{print $1}')

    # Extract destination host from CONNECT or GET request
    dst=$(echo "$line" | grep -oE '"(CONNECT|GET) [^ /:]+' | awk '{print $2}')

    if echo "$src" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' && \
       [ -n "$dst" ]; then

        logger -t "$LOG_TAG" "Sending src: $src, dst: $dst"
        curl -s -X POST "$API_URL" -H "$CONTENT_TYPE" \
             -d "{\"src\": \"$src\", \"dst\": \"$dst\"}"
    fi
done

