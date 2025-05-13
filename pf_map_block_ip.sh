#!/bin/sh

LOG_FILE="/var/log/pfblockerng/ip_block.log"
API_URL="http://10.1.1.15:8080/add_ip/"
CONTENT_TYPE="Content-Type: application/json"

echo "[INFO] Watching $LOG_FILE for IP entries..."

# Cleanup function to handle script exit
#cleanup() {
    #echo "[INFO] Cleaning up..."
    #kill %tail
    #exit 0
#}

# Trap CTRL+C to call cleanup function
trap cleanup INT

# Main loop to process log entries
tail -F "$LOG_FILE" | while read -r line; do
    # Extract the 10th field (destination IP) from the log line
    ip=$(echo "$line" | awk -F',' '{print $10}')

    # If an IP is found, send it to the API
    if [ -n "$ip" ]; then
        echo "[INFO] Sending IP: $ip"
        # Send the IP as a JSON object to the API
        curl -s -X POST "$API_URL" -H "$CONTENT_TYPE" -d "{\"ip\": \"$ip\"}"
    fi
done

