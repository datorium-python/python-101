from http.server import BaseHTTPRequestHandler, HTTPServer


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    # We have: GET, POST, PUT, DELETE
    # We goona use: GET, POST

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request".encode('utf-8'))


host = ''
port = 8000
HTTPServer((host, port), HandleRequests).serve_forever()
