from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        path = self.url().path

        if path == "/":
            try:
                with open("home.html", "r", encoding="utf-8") as f:
                    content = f.read()

                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))

            except FileNotFoundError:
                self.send_error(500, "home.html no encontrado")

        else:
            self.send_error(404, "Not Found")

    # def get_response(self):
    #    split_url = self.url().path.split("/")
    #
    #   proyecto = split_url[2] if len(split_url) > 2 else "Desconocido"
    #   autor = self.query_data().get("autor", "Desconocido")
    #
    #    return f"""
    #    <h1>Proyecto: {proyecto} Autor: {autor}</h1>
    #    p>URL Parse Result : {self.url()}</p>
    #    <p>Path Original: {self.path}</p>
    #    <p>Headers: {self.headers}</p>
    #    <p>Query: {self.query_data()}</p>
    #    """


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
