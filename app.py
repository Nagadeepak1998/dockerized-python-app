from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print('Server running on http://localhost:8080/')
    server.serve_forever()
