#!/bin/sh

# Logs to journalctl. Watch with e.g. journalctl -t SNAP_NAME -f
log()
{
    logger -t ${SNAP_NAME} -- "$1"
}

restart_erigon()
{
    erigon_status="$(snapctl services erigon)"
    current_status=$(echo "$erigon_status" | awk 'NR==2 {print $3}')
    if [ "$current_status" = "active" ]; then
        snapctl restart erigon
    fi
}
