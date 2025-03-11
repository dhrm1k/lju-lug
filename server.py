from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def run(server_class=HTTPServer, handler_class=Handler, port=8000, directory="public"):
    # Ensure directory exists
    if not Path(directory).exists():
        print(f"Error: Directory '{directory}' not found.")
        print("Please run the static site generator first.")
        return

    # Change to the specified directory
    os.chdir(directory)
    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print(f"Serving at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        httpd.server_close()

if __name__ == '__main__':
    run()