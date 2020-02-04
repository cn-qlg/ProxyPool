# from proxy_parser.proxy_parser_base import ProxyParserBase
from proxy_parser.proxy_parser_base import ProxyParserBase
import requests
from bs4 import BeautifulSoup


class XiciProxyParser(ProxyParserBase):
    def __init__(self):
        super().__init__()
        self.start_urls = ["https://www.xicidaili.com/wn/",
                           "https://www.xicidaili.com/wt/"]

    # def get_response(self, url):
    #     return requests.get(url).text

    def parse_response(self, response):
        bs = BeautifulSoup(response, features="html.parser")
        rows = list(bs.findAll("tr"))[1:]
        ips = []
        for row in rows:
            rowdata = list(row.findAll("td"))

            try:
                country_img = rowdata[0].img
                if country_img:
                    country = country_img["alt"].lower()
                else:
                    country = "default"
                # country = rowdata[0].img["alt"]
                ip = rowdata[1].text.strip()
                port = rowdata[2].text.strip()
                location = rowdata[3].text.strip()
                is_anonymous = True if rowdata[4].text.strip()  == "高匿" else False
                https = False if rowdata[5].text.strip().find("HTTPS") == 0 else True
                ipdata = {"ip": ip, "port": port, "https": https, "country":country, "is_anonymous":is_anonymous, "location":location}
                print(ipdata)
                ips.append(ipdata)
            except Exception:
                print(rowdata)
                print(row.text)
                print(rowdata[0])
        print(len(ips))
        return ips

    # def get_proxies(self):
    #     print("11")
    #     print(ProxyParserBase.StartUrls)
    #     for url in ProxyParserBase.StartUrls:
    #         self.parse_response(self.get_response(url))


if __name__ == "__main__":

    parser = XiciProxyParser()
    print(parser)
    print(parser.get_proxies)
    parser.get_proxies()
