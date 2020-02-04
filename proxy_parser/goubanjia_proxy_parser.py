from proxy_parser.proxy_parser_base import ProxyParserBase
import requests
from bs4 import BeautifulSoup, NavigableString 


def tr_and_has_class(tag):
    return tag.name == "tr" and tag.has_attr('class')

def get_text(tag):
    if type(tag) is NavigableString:
        return tag.string
    elif tag.has_attr("style") and "none" in tag["style"]:
        return ""
    else:
        return tag.text

class GoubanjiaProxyParser(ProxyParserBase):
    def __init__(self):
        super().__init__()
        self.start_urls = ["http://www.goubanjia.com/"]

    def parse_response(self, response):
        bs = BeautifulSoup(response, features="html.parser")
        rows = bs.findAll(tr_and_has_class)
        ip_list = []
        for row in rows:
            tds = list(row.findAll("td"))
            data_list = []
            for child in tds[0].contents:
                data_list.append(get_text(child))
            full_ip = "".join(data_list)
            ip, port = full_ip.split(":")      
            is_anonymous = True if tds[1].text.strip()  in ["高匿", "匿名"] else False
            https = False if tds[2].text.strip() == "https" else True
            location = "".join([stringdata for stringdata in tds[3].stripped_strings])
            country = "cn" if "中国" in location else location
            ip_data = {"ip": ip, "port": port, "full_ip": f"{ip}:{port}","https": https, "country":country, "is_anonymous":is_anonymous, "location":location}
            print(ip_data)
            ip_list.append(ip_data)
        return ip_list
