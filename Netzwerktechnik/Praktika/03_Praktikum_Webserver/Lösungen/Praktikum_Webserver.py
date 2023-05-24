from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class SimpleWebserver(BaseHTTPRequestHandler):
    def do_GET(self):

        status = 200
        if self.path == "/info":
            body = "This is a info page"
        elif self.path == "/":
            body = "This is the default page."
        else:
            body = "404 not found!"
            status = 404

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(f'''
            <html><head><title>https://pythonbasics.org</title></head>
            <body>
                <p>{body}</p>
            </body></html>
        ''', "utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_length)
        print(post_body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), SimpleWebserver)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
