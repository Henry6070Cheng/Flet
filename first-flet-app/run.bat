@echo off
chcp 65001
set PYTHONIOENCODING=utf-8
set LANG=zh_CN.UTF-8
flet run --web --web-renderer html --web-port 8000 --web-hostname localhost main.py 
mkdir web\fonts
copy C:\Windows\Fonts\simsun.ttc web\fonts\