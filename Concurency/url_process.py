import multiprocessing, requests


def fetch_url(url):
    response = requests.get(url)
    with open('result_process.txt', "w", encoding="utf-8") as f:
        f.write(response.text)


urls = ["https://www.example.com",
        "https://slovnyk.ua/index.php?swrd=бруквяний"
        "https://github.com/EugenMytrik/Concurency",
        "https://black.readthedocs.io/en/stable/integrations/github_actions.html",]


if __name__ == "__main__":
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))  
        process.start()
        process.join()