from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json

# Create a simple database and table if not exists
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT)")
cursor.execute("INSERT INTO messages (message) VALUES ('Hello from the database!')")
conn.commit()
conn.close()


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

        elif self.path == "/data":
            # Fetch data from database
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT message FROM messages ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            conn.close()

            message = row[0] if row else "No data found"

            # Send JSON response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps({"message": message}), "utf8"))


# Start the server
with HTTPServer(("", 8000), handler) as server:
    print("Server running on port 8000...")
    server.serve_forever()
