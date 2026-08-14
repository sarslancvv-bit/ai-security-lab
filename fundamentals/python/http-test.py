import requests


# GET
r_get = requests.get("https://api.github.com/events", timeout=5)
print("GET status:", r_get.status_code)
print("GET body (first 200 chars):", r_get.text[:200])

# POST
r_post = requests.post("https://httpbin.org/post", data={"key": "value"}, timeout=5)
r_post.raise_for_status()
print("POST result:", r_post.json())

# PUT
r_put = requests.put("https://httpbin.org/put", data={"key": "value"}, timeout=5)
r_put.raise_for_status()
print("PUT result:", r_put.json())

# DELETE
r_delete = requests.delete("https://httpbin.org/delete", timeout=5)
r_delete.raise_for_status()
print("DELETE status:", r_delete.status_code)

# HEAD - no body, only check status/headers
r_head = requests.head("https://httpbin.org/get", timeout=5)
print("HEAD status:", r_head.status_code)
print("HEAD headers:", r_head.headers)

# OPTIONS - also often no JSON body
r_options = requests.options("https://httpbin.org/get", timeout=5)
print("OPTIONS status:", r_options.status_code)
print("OPTIONS allow header:", r_options.headers.get("allow"))




payload = {"key1": "value1",
           "key2": "value2" 
}

r= requests.get("https://httpbin.org/get", params= payload)

print(r.url)

https://example.com/search?q=python&page=2

?     → parametreler burada basliyor
q     → key
python → value
&     → başka parametre geliyor
page  → ikinci key
2     → ikinci value




params = {"q": "python",
          "page": 2
}

r_get= requests.get("https://example.com/search",
                    params=params
)

print(r_get.url)

parameters = {"sami": "isim",
              "22" : "yas"
}

r_get2 = requests.get("https://example.com/search",
          params= parameters
)
print(r_get2.url)

params1 = {"key1": "value1",
           "key2" : ["value2", "value3"]
}

r_get3 = requests.get("https://example.com/search",
                      params= params1
)

print(r_get3.url)


r = requests.get("https://api.github.com/events")

print(r.text)

print(r.encoding)

r.encoding = 'ISO-8859-1'

print(r.text)

print(r.content)


import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://httpbin.org/image/jpeg", timeout=10)
r.raise_for_status()

print()
print(r.content[:50])
print()

print("Status:", r.status_code)
print("Content-Type:", r.headers.get("content-type"))


image = Image.open(BytesIO(r.content))
image.save("save.jpg")
print("Resim kaydedildi.")

r = requests.get("https://api.github.com/events")

r.raise_for_status()

data = r.json()

print(type(data))

print(data[0])

r = requests.get("https://api.github.com/events", stream=True)

print(r.raw)

print(r.raw.read(10))

with open(filename,"wb") as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

url = "https://httpbin.org/anything"

params = {
    "search": "python",
    "page": 2
}

headers = {
    "User-Agent": "MyLearningApp/1.0",
    "Accept": "application/json"
}

body = {
    "username": "sami",
    "language": "python"
}

r = requests.post(
    url,
    params=params,
    headers=headers,
    json=body,
    timeout=5
)

r.raise_for_status()

result = r.json()

print("URL:")
print(result["url"])

print("\nHEADERS:")
print(result["headers"])

print("\nJSON BODY:")
print(result["json"])


payload = {"language": ["Python","Java","JavaScript"]}
r = requests.post("https://httpbin.org/post", data=payload)

print(r.text)

r = requests.post("https://httpbin.org/post", data="HELLO SAMi")

print(r.text)

pload = {
    "username": "sami",
    "age": 22
}

r = requests.post(
    "https://httpbin.org/post",
    json=pload
)



import requests

payload = {
    "username": "sami",
    "age": "22"
}

r = requests.post(
    "https://httpbin.org/post",
    json=payload
)

result = r.json()

print("FORM:")
print(result["form"])

print("JSON:")
print(result["json"])

r = requests.get("https://httpbin.org/get")

print(r.status_code)

r.status_code == requests.codes.ok

print(requests.codes.ok)

r = requests.get("https://httpbin.org/status/404")

print(r.status_code)

r.raise_for_status()

session = requests.Session()

# Server bize bir cookie versin
session.get(
    "https://httpbin.org/cookies/set",
    params={"theme": "dark"}
)

# Session'da hangi cookie var?
print("Cookies:")
print(session.cookies)

# Başka bir request gönder
r = session.get("https://httpbin.org/cookies")

print("Server'ın gördüğü:")
print(r.json())

# GET
r_get = requests.get("https://api.github.com/events", timeout=5)
print("GET status", r_get.status_code)
print("GET body (first 200 chars):", r_get.text[:200])

# POST
r_post = requests.post("https://httpbin.org/post",data={"key": "value" },timeout= 5)
r_post.raise_for_status()
print("POST result:", r_post.json())

# PUT
r_put = requests.put("https://httpbin.org/put", data={"key": "value"}, timeout=5)
r_put.raise_for_status()
print("PUT result:", r_put.json())
"""
"""
# DELETE
r_delete = requests.delete("https://httpbin.org/delete", timeout=5)
r_delete.raise_for_status()
print("DELETE status:", r_delete.status_code)

# HEAD - no body, only check status/headers
r_head = requests.head("https://httpbin.org/get", timeout=5)
print("HEAD status:", r_head.status_code)
print("HEAD headers:", r_head.headers)
"""
# OPTIONS - also often no JSON body
r_options = requests.options("https://httpbin.org/get", timeout=5)
print("OPTIONS status:", r_options.status_code)
print("OPTIONS allow header:", r_options.headers.get("allow"))

try:
    r_fail = requests.get("https://httpbin.org/status/404", timeout=5)
    r_fail.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Hata yakalandi:", e)


r_json = requests.post(
    "https://httpbin.org/post",
    json={"mesaj": "merhaba", "hafta": 1},
    timeout=5
)
r_json.raise_for_status()
print(r_json.json())
