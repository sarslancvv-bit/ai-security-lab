# HTTP — Complete Summary

## 1. What is HTTP?

HTTP (HyperText Transfer Protocol) is an application-layer protocol used for communication between a client and a server.

**Basic model:**

```
CLIENT                         SERVER

       HTTP Request
       GET /products
──────────────────────────────►

       HTTP Response
       200 OK + data
◄──────────────────────────────
```

HTTP can transfer HTML, JSON/API data, images, videos, form data, files, etc.

---

## 2. HTTP, TCP and TLS

Traditionally:

```
HTTP        → what is being communicated
 ↓
TLS         → encrypts/protects it (HTTPS)
 ↓
TCP         → reliably transports it
 ↓
IP          → routes it across networks
```

So traditionally:

```
HTTP + TLS + TCP ≈ HTTPS
```

Modern **HTTP/3** uses **QUIC over UDP** instead of TCP.

---

## 3. Client / User-Agent

The client initiates HTTP requests. A **user-agent** is software acting on behalf of the user.

Examples:
- Chrome
- Firefox
- curl
- Postman
- Python `requests`
- Googlebot

```bash
curl https://example.com
```

`curl` is acting as the HTTP client.

---

## 4. Loading one webpage means many HTTP requests

Opening `https://shop.com` might produce:

```
GET /              → HTML
GET /style.css     → CSS
GET /app.js        → JavaScript
GET /logo.png      → image
GET /api/products  → JSON
```

The browser downloads all these resources and combines them into the webpage you see.

JavaScript can later make additional requests using `fetch()` without reloading the page.

---

## 5. Web Server

The server receives requests and generates responses.

```
Browser
   │
   │ GET /products/42
   ▼
Web Server
   │
   ├── Database
   ├── Cache
   └── Other services
   │
   ▼
200 OK
{"name":"Keyboard"}
```

A "server" doesn't necessarily mean one physical computer. Large websites may have thousands of servers.

---

## 6. Proxies

A proxy is an intermediary:

```
Client → Proxy → Server
```

It can perform:
- Caching
- Filtering
- Authentication
- Logging
- Load balancing
- Forwarding

This matters for cybersecurity because **Burp Suite** can act as an HTTP proxy:

```
Browser
   ↓
Burp
   ↓
Server
```

allowing you to inspect HTTP requests and responses in authorized environments.

---

## 7. Caching

Caching means storing a response so it can potentially be reused.

Server:

```
Cache-Control: max-age=3600
```

means roughly: *this response may be considered fresh for 1 hour under the applicable caching rules.*

Instead of:

```
Browser → Server → download logo
Browser → Server → download logo again
```

you can potentially have:

```
Browser → download logo
        ↓
      CACHE

Later → use cached logo
```

---

## 8. HTTP is extensible

HTTP functionality can be extended through headers.

```http
GET / HTTP/1.1
Host: example.com
Accept-Language: fr
Authorization: Bearer abc123
```

Headers provide additional information without changing HTTP's fundamental request/response model.

Tested with:

```bash
curl --http1.1 -v \
-H "Accept-Language: fr" \
https://developer.mozilla.org/
```

MDN responded with:

```
302 Found
Location: /fr/
```

Your header affected the server's response.

---

## 9. HTTP is stateless

HTTP requests are fundamentally independent.

```
Request #1
GET /something

Request #2
GET /account
```

HTTP itself doesn't automatically say *these requests belong to the same logged-in user.*

Web applications therefore use mechanisms such as cookies and sessions.

---

## 10. Cookies and sessions

You log in:

```
POST /login
```

Server creates a session:

```
ABC123 → Sami
```

and responds:

```
Set-Cookie: session=ABC123
```

Browser stores it. Future request:

```
GET /account
Cookie: session=ABC123
```

Server sees:

```
ABC123 → Sami
```

**Therefore:** HTTP is stateless, but applications can create stateful sessions using mechanisms such as cookies.

---

## 11. Same-Origin Policy

Browsers don't let JavaScript freely access data from unrelated origins.

An **origin** is essentially: `scheme + host + port`

```
https://shop.com:443
```

These are **different origins**:

```
https://shop.com
https://api.example.com
```

The Same-Origin Policy provides an important browser security boundary.

---

## 12. CORS

Sometimes different origins legitimately need to communicate.

Frontend: `https://myshop.com`
API: `https://api.myshop-services.com`

API can respond:

```
Access-Control-Allow-Origin: https://myshop.com
```

telling the browser that this origin may access the response under CORS rules.

| Concept | Description |
|---|---|
| Same-Origin Policy | Default browser restriction |
| CORS | Controlled cross-origin permissions |

**Most importantly:** CORS is enforced by browsers. That's why `curl` generally isn't blocked by CORS like browser JavaScript can be.

---

## 13. Fetch API

JavaScript can make HTTP requests using:

```js
fetch("/api/products")
```

which could produce:

```
GET /api/products
```

You can also POST:

```js
fetch("/api/comments", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        text: "Hello"
    })
})
```

Conceptually:

```http
POST /api/comments
Content-Type: application/json

{"text":"Hello"}
```

So:

```
JavaScript
 ↓
fetch()
 ↓
Browser
 ↓
HTTP request
 ↓
Server
```

---

## 14. Server-Sent Events (SSE)

SSE lets a server continuously send events to a connected client.

```
Client ─── connect ───► Server

Client ◄── event ───── Server
Client ◄── event ───── Server
Client ◄── event ───── Server
```

Examples: live scores, notifications, live status updates.

SSE is primarily `Server → Client`, whereas WebSockets allow ongoing `Server ↔ Client`.

---

## 15. HTTP Request Structure

A request generally contains:

```
METHOD + TARGET/PATH + VERSION
HEADERS

BODY (optional)
```

Example:

```http
POST /users HTTP/1.1
Host: example.com
Content-Type: application/json
Accept: application/json

{
    "name": "Sami"
}
```

Breaking it down:

| Part | Value |
|---|---|
| Method | `POST` |
| Path | `/users` |
| Version | `HTTP/1.1` |
| Header | `Host` |
| Header | `Content-Type` |
| Header | `Accept` |
| Body | `{"name":"Sami"}` |

---

## 16. HTTP Response Structure

A response generally contains:

```
VERSION + STATUS
HEADERS

BODY (optional)
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "name": "Sami"
}
```

Breaking it down:

| Part | Value |
|---|---|
| Version | `HTTP/1.1` |
| Status code | `200` |
| Reason phrase | `OK` |
| Header | `Content-Type` |
| Body | `{"name":"Sami"}` |

---

## 17. Important HTTP methods

| Method | Purpose | Example |
|---|---|---|
| `GET` | Retrieve | `GET /users/42` — Give me user 42 |
| `POST` | Submit/process | `POST /users` `{"name":"Sami"}` — Process this data, perhaps creating a user |
| `PUT` | Replace | `PUT /users/42` `{"name":"Sami","age":23}` — Replace the target representation |
| `PATCH` | Partially modify | `PATCH /users/42` `{"age":23}` — Change part of user 42 |
| `DELETE` | Delete | `DELETE /users/42` — Delete user 42 |
| `HEAD` | GET without response body | `HEAD /image.png` — Get metadata/headers only |
| `OPTIONS` | Communication options | `OPTIONS /users` — Discover options; important for CORS preflight |
| `CONNECT` | Tunnel | `CONNECT example.com:443` — Commonly associated with proxies |
| `TRACE` | Diagnostics | Asks for a loop-back of the request for diagnostic purposes |

---

## 18. Safe methods

Safe does **NOT** mean cybersecurity-safe. It means: *the client isn't asking the server to change resource state.*

| Method | Safe? |
|---|---|
| GET | ✅ |
| HEAD | ✅ |
| OPTIONS | ✅ |
| TRACE | ✅ |
| POST | ❌ |
| PUT | ❌ |
| PATCH | ❌ |
| DELETE | ❌ |
| CONNECT | ❌ |

Example: `GET /users/42` just retrieves information → safe.
`DELETE /users/42` requests a change → not safe.

---

## 19. Idempotent methods

Idempotent means repeating the same request has the same intended effect on server state as doing it once.

Example:

```
DELETE /users/42
```

Once: user gone. Ten times: user still gone.

| Method | Safe? | Idempotent? |
|---|---|---|
| DELETE | ❌ | ✅ |
| PUT | ❌ | ✅ |
| POST | ❌ | ❌ (usually) |

`PUT /users/42` with `{"name":"Sami"}` — sending the same replacement repeatedly leaves the same intended final representation.

`POST /orders` — once creates Order #1, again creates Order #2, so repeating it may create additional effects.

---

## 20. Cacheable

Cacheable means a response may be stored and reused according to HTTP caching rules.

Classic example:

```
GET /logo.png
```

Server:

```
Cache-Control: max-age=3600
```

A cache may reuse that response for an appropriate period instead of downloading it again.

Strongly associate caching with `GET` and `HEAD`. `POST`/`PATCH` responses can be cacheable under specific conditions, but that's much less common.

---

## 21. Important status code families

| Range | Meaning | Examples |
|---|---|---|
| 1xx | Information | — |
| 2xx | Success | `200 OK`, `201 Created`, `204 No Content` |
| 3xx | Redirection | `301 Moved Permanently`, `302 Found` |
| 4xx | Client-side/request problem | `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` |
| 5xx | Server-side problem | `500 Internal Server Error` |

Especially remember:

- **401** → authentication is missing/invalid → *"Who are you?"*
- **403** → server refuses the action despite the requester's identity/context → *"You can't access/do this."*

---

## 22. HTTP versions and connections

Very simplified evolution:

| Version | Connection behavior |
|---|---|
| HTTP/1.0 | Often separate TCP connections |
| HTTP/1.1 | Persistent TCP connections |
| HTTP/2 | Multiplex multiple streams efficiently over a TCP connection |
| HTTP/3 | QUIC instead of TCP |

Don't spend too much time on this yet.

---

## The entire topic in one picture

If you understand this, you're in good shape:

```
                     CLIENT
              Browser / curl / app
                       │
                       │
                HTTP REQUEST
                       │
                POST /login
                Host: shop.com
                Content-Type: application/json
                       │
                {"user":"sami"}
                       │
                       ▼
                [TLS for HTTPS]
                       │
                       ▼
             [Transport/network]
                       │
                       ▼
             Proxy/CDN/etc. maybe
                       │
                       ▼
                    SERVER
                       │
                 application
                 database/cache
                       │
                       ▼
                HTTP RESPONSE
                       │
                 HTTP/1.1 200 OK
                 Set-Cookie: ...
                 Content-Type: ...
                       │
                 {"success":true}
                       │
                       ▼
                     CLIENT
```

---

## Highest-priority concepts

For your HTTP deep-dive goal, know these without notes:

- Request vs. response
- Method, path, headers, body
- `GET` / `POST` / `PUT` / `PATCH` / `DELETE`
- Status codes (especially `200`/`201`/`400`/`401`/`403`/`404`/`500`)
- Cookies / sessions
- Safe vs. idempotent
- Basic Same-Origin Policy / CORS
