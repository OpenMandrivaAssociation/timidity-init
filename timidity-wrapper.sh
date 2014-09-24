#!/bin/bash

OPTIONS="-iAq -Os"

# Parse options
if [[ "$BUFNUM" =~ "[0-9]+" ]] && [[ "$BUFSIZE" =~ "[0-9]+" ]]; then
        OPTIONS="${OPTIONS} --buffer-fragments=${BUFNUM},${BUFSIZE}"
fi
[[ "$SAMPLERATE" =~ "[0-9]+" ]] && OPTIONS="$OPTIONS --sampling-freq=$SAMPLERATE"
[ "$ANTIALIAS" = "true" ] && OPTIONS="$OPTIONS --anti-alias"
[[ "$PRIORITY" =~ "[0-9]+" ]] && OPTIONS="$OPTIONS --realtime-priority=$PRIORITY"
[ -n "$EXTRA_OPTIONS" ] && OPTIONS="$OPTIONS $EXTRA_OPTIONS"

exec timidity $OPTIONS
