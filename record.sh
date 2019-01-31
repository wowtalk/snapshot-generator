#!/bin/bash

trap "exit" INT TERM ERR
trap "kill 0" EXIT

# get stream
STREAM_URL=$(python livestream_metadata.py)
echo "Stream URL: $STREAM_URL"

# start sync
while sleep 1; do 
  echo "======> Resuming sync snapshots ..."
  aws s3 sync snapshots/ s3://wow-livestream-images
done &

# start convert
echo "======> Resuming snapshot generation ..."
ffmpeg -i $STREAM_URL -vf fps=1/3 -start_number $(ls snapshots | wc -l) snapshots/snapshot-%05d.png -hide_banner

wait
