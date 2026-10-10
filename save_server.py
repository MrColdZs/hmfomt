from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        filename = data['filename'].replace('.gif', '.webp').replace('.png', '.webp')
        b64 = data['image'].split(',')[1]
        
        filepath = os.path.join('items_clean', filename)
        with open(filepath, 'wb') as f:
            f.write(base64.b64decode(b64))
            
        print(f"Saved {filepath}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')
        
    def log_message(self, format, *args):
        pass

HTTPServer(('127.0.0.1', 8001), SimpleHTTPRequestHandler).serve_forever()
