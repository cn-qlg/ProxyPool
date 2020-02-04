from proxy_parser.proxy_parser_base import ProxyParserBase
import requests
from bs4 import BeautifulSoup, NavigableString


class KuaidailiProxyParser(ProxyParserBase):
    def __init__(self):
        super().__init__()
        self.start_urls = ["https://www.kuaidaili.com/free/",
                           "https://www.kuaidaili.com/free/intr/"]

    def parse_response(self, response):
        bs = BeautifulSoup(response, features="html.parser")
        rows = list(bs.findAll("tr"))
        ip_list = []
        for row in rows[1:]:
            tds = list(row.findAll("td"))
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            is_anonymous = True if tds[2].text.strip() == "高匿名" else False
            https = False if tds[3].text.strip() == "https" else True
            location = tds[4].text.strip()
            country = "cn" if "中国" in location else location
            ip_data = {"ip": ip, "port": port, "full_ip": f"{ip}:{port}", "https": https,
                       "country": country, "is_anonymous": is_anonymous, "location": location}
            print(ip_data)
            ip_list.append(ip_data)
        print(len(ip_list))
        return ip_list
