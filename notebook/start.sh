#!/bin/bash
if [ ! -f /app/data/trips.csv ]; then
  cp /app/trips.csv /app/data
fi

exec "jupyter" "notebook" "--ip='*'" "--port=8888" "--no-browser" "--allow-root"
