#!/bin/bash
mkdir -p /app/output

MODE=${MODE:-1A}

if [ "$MODE" == "1A" ]; then
    echo "🔁 Running Round 1A (Outline Extractor)..."
    for file in /app/input/*.pdf; do
        filename=$(basename "$file" .pdf)
        python3 -m app.run "$file" "/app/output/$filename.json"
    done

elif [ "$MODE" == "1B" ]; then
    echo "🧠 Running Round 1B (Persona-Based Intelligence)..."
    python3 -m app.run_b

else
    echo "❌ Invalid MODE specified. Use MODE=1A or MODE=1B."
    exit 1
fi
