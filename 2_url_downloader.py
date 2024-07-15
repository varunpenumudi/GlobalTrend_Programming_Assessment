import requests


def download_content(urls, timeout=3):
    contents = {}
    for url in urls:
        retries = 3
        while retries:
            try:
                response = requests.get(url, timeout=timeout)
                response.raise_for_status()
                contents[url] = response.content
                break
            except requests.exceptions.HTTPError as err:
                print(f"Http Error Occured {err}")
            except requests.exceptions.Timeout as err:
                print(f"Request Timed Out {err}")
            except Exception as err:
                print(f"Error Occured: {err}")

            print(f"Retrying: {4-retries}/3 attempt")
            retries -= 1
        else:
            contents[url] ="Failed to retrive contents."
    
    return contents

urls = [
    "https://httpbin.org/status/404",
    "https://httpbin.org/delay/5",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/encoding/utf8",
    "http://invalid_url"
]


contents = download_content(urls)

print("-"*150)
print("DOWNLOADED CONTENTS: ")
for url, content in contents.items():
    if content and len(content) > 50:
        print(f"{url}:      {content[:50]}.........")
    else:
        print(f"{url}:      {content}")
print("-"*150)
