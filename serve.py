#!/usr/bin/env python3
"""
Simple HTTP server for FIFA World Cup Tracker
Run with: python3 serve.py
"""
import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ FIFA World Cup Tracker Server Running!")
        print(f"📍 URL: http://localhost:{PORT}")
        print(f"📂 Serving: {Path.cwd()}")
        print(f"\n🚀 Opening browser...")
        print(f"Press Ctrl+C to stop the server\n")
        
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            pass
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Thanks for using FIFA World Cup Tracker!")

if __name__ == "__main__":
    main()
