import requests

def TestFunc():
    url = 'http://google.com'
    rsp = requests.get(url)
    print(f'HTTP GET {url}: -> return status_code {rsp.status_code}')
