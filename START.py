#!/usr/bin/env python3
"""
Pistachio Website — Local Server Launcher
Double-click this file or run: python3 START.py
"""
import http.server, webbrowser, os, threading, time

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        pass  # silent

def open_browser():
    time.sleep(0.8)
    webbrowser.open(f'http://localhost:{PORT}')

print(f"🍃 Pistachio — Démarrage du serveur sur http://localhost:{PORT}")
print(f"   Appuyez sur Ctrl+C pour arrêter\n")

threading.Thread(target=open_browser, daemon=True).start()

with http.server.HTTPServer(('', PORT), Handler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
