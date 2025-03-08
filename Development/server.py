from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Serve the HTML file
            try:
                with open("index.html", "r") as file:
                    content = file.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(content, "utf8"))

            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"404 Not Found: index.html is missing")


# Start the server
with HTTPServer(("", 8000), handler) as server:
    print("Server running on port 8000...")
    server.serve_forever()
