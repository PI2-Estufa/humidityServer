#!/bin/sh
echo Starting rabbit
sleep 10
nameko run --config config.yml humidity_server
