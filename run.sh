#!/bin/bash
mkdir -p /app/output
for file in /app/input/*.pdf; do
    filename=$(basename "$file" .pdf)
    python3 -m app.run "$file" "/app/output/$filename.json"
done