import time

import requests


def fetch(url):
    response = requests.get(url)
    return response.text


def main():
    url = "http://localhost:8000/get_all_students/"
    num_requests = 1000

    start_time = time.time()

    for _ in range(num_requests):
        fetch(url)

    end_time = time.time()

    print(f"Completed {num_requests} requests in {end_time - start_time:.2f} seconds")
    print(f"Average time per request: {(end_time - start_time) / num_requests:.4f} seconds")


if __name__ == "__main__":
    main()
