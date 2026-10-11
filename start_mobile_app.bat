@echo off
title Planfit Mobile Workout Server
cd /d "%~dp0mobile_app"
python serve_mobile.py
pause
