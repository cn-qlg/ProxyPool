import requests


class HttpUtil:

    @staticmethod
    def get(url, encoding=None):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        if not encoding:
            return requests.get(url, headers=headers).text
        else:
            resp = requests.get(url)
            resp.encoding = encoding
            return resp.text
