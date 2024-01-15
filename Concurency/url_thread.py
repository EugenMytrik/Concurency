import threading, requests


def fetch_url(url):
    response = requests.get(url)
    with open('result_thread.txt', "w", encoding="utf-8")  as f:
        f.write(response.text)


urls = ["https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",
        "https://www.example.com",]


if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        thread.join()