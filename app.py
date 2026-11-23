import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

ITEMS = [
    {"id": 1, "title": "Навигация в терминале", "topic": "linux"},
    {"id": 2, "title": "Права доступа и chmod", "topic": "linux"},
    {"id": 3, "title": "Процессы и systemd", "topic": "linux"},
    {"id": 4, "title": "Основы контейнеров Podman", "topic": "podman"},
    {"id": 5, "title": "Сборка образов через Containerfile", "topic": "podman"},
    {"id": 6, "title": "HTTP-сервер на стандартном Python", "topic": "python"},
]


class APIHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlsplit(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/health":
            self.send_json(200, {"status": "ok"})
            return

        if path == "/api/items":
            topics = query.get("topic")
            if topics:
                target_topic = topics[0]
                filtered = [item for item in ITEMS if item["topic"] == target_topic]
                self.send_json(200, {"items": filtered})
            else:
                self.send_json(200, {"items": ITEMS})
            return

        if path == "/api/summary":
            by_topic = {}
            for item in ITEMS:
                topic = item["topic"]
                by_topic[topic] = by_topic.get(topic, 0) + 1
            self.send_json(200, {"total": len(ITEMS), "by_topic": by_topic})
            return

        self.send_json(404, {"error": "Not Found"})


def run():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    server = ThreadingHTTPServer((host, port), APIHandler)
    print(f"Server started on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
