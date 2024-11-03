from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Render! The server is running.")

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, Handler)
    print("Server running on port 8080...")
    httpd.serve_forever()
