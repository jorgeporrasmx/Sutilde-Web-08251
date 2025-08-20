from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
        print(f"Serving at port {PORT} with caching disabled")
        httpd.serve_forever() 