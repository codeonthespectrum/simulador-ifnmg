#!/usr/bin/env python3
"""
Servidor HTTP simples para rodar o simulador IFNMG
Execute: python3 servidor.py
Acesse: http://localhost:8000
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Muda para o diretório do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

print(f"🎓 Simulador IFNMG")
print(f"=" * 40)
print(f"Servidor iniciado em: http://localhost:{PORT}")
print(f"Pressione Ctrl+C para parar")
print(f"=" * 40)

# Abrir navegador automaticamente
webbrowser.open(f'http://localhost:{PORT}')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServidor encerrado.")
