import abc
import sys
sys.path.append('..')
print(sys.path)
from utils.httputil import HttpUtil

class ProxyParserBase(metaclass=abc.ABCMeta):

    def __init__(self):
        self.start_urls = []

    def get_response(self, url):
        return HttpUtil.get(url)

    @abc.abstractmethod
    def parse_response(self, response):
        pass

    def get_proxies(self):
        print("ProxyParserBase get_proxies")
        for url in self.start_urls:
            self.parse_response(self.get_response(url))
