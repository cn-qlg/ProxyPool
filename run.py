from proxy_parser.xici_proxy_parser import XiciProxyParser

if __name__ == "__main__":

    parser = XiciProxyParser()
    print(parser)
    print(parser.get_proxies)
    parser.get_proxies()
