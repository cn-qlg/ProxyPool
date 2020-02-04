from proxy_parser.xici_proxy_parser import XiciProxyParser
from proxy_parser.goubanjia_proxy_parser import GoubanjiaProxyParser
from proxy_parser.kuaidaili_proxy_parser import KuaidailiProxyParser
from proxy_parser.iphai_proxy_parser import IpHaiProxyParser

if __name__ == "__main__":

    parser = IpHaiProxyParser()
    print(parser)
    print(parser.get_proxies)
    parser.get_proxies()
