#!/bin/sh
./otelcol-contrib --config /app/config.yaml &
python main.py