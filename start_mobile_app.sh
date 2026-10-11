#!/usr/bin/env bash
cd "$(dirname "$0")/mobile_app" || exit
python serve_mobile.py
