from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

with open("home.html", encoding="utf-8") as f:
    HOME = f.read()

with open("1.html", encoding="utf-8") as f:
    PROYECTO1 = f.read()

contenido = {
    "/": HOME,
    "/proyecto/1": PROYECTO1,
    "/proyecto/2": "<h1>Proyecto 2</h1>",
    "/proyecto/3": "<h1>Proyecto 3</h1>",
}

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    # def query_data(self):
    #     return dict(parse_qsl(self.url().query))

    def do_GET(self):
        path = self.url().path

        if path in contenido:

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(contenido[path].encode("utf-8"))
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
