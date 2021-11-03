
import re
import requests



def test():
    url = 'https://console.aiven.io/signup.html'  # 'http://kafka.apache.org/'
    rsp = requests.get(url)

    # pattern = r'<title>Apache\s*Kafka</title>'
    pattern = r'Sign up for your free 30 day trial!'
    sr = re.search(pattern, rsp.text)
    if sr:
        print(sr.group())
    else:
        print('nothing found')

    pattern = r'something else'
    sr = re.search(pattern, rsp.text)
    if sr:
        print(sr.group())
    else:
        print('nothing found')


test()

