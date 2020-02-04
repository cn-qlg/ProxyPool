from proxy_parser.xici_proxy_parser import XiciProxyParser
from proxy_parser.goubanjia_proxy_parser import GoubanjiaProxyParser

if __name__ == "__main__":

    parser = XiciProxyParser()
    print(parser)
    print(parser.get_proxies)
    parser.get_proxies()
