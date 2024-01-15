import concurrent.futures, requests, time


def fetch_url(url):
    return requests.get(url)


if __name__ == "__main__":
    url = "https://www.example.com"
    num_requests = 10

    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        executor.map(fetch_url, [url] * num_requests)
        end_time = time.time()

    print(f"Time taken for {num_requests} requests: {end_time - start_time} seconds")