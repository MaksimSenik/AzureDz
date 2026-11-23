@MaksimSenik ➜ /workspaces/AzureDz (master) $ curl -i "127.0.0.1:8001/api/items?topic=podman"
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.14.2
Date: Mon, 23 Nov 2026 09:16:21 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 191

{"items": [{"id": 4, "title": "Основы контейнеров Podman", "topic": "podman"}, {"id": 5, "title": "Сборка образов через Containerfile", "topic": "podman"}]}
{"items": []}

@MaksimSenik ➜ /workspaces/AzureDz (master) $ curl -i "127.0.0.1:8001/api/items?topic=unknown"
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.14.2
Date: Mon, 23 Nov 2026 09:17:29 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 13

@MaksimSenik ➜ /workspaces/AzureDz (master) $ curl -i "127.0.0.1:8001/api/summary"
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.14.2
Date: Mon, 23 Nov 2026 09:18:10 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 64

{"total": 6, "by_topic": {"linux": 3, "podman": 2, "python": 1}}