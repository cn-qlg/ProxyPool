from peewee import *

db = MySQLDatabase(host='127.0.0.1', database='meituan', user='root',
                   password='testtest', charset='utf8')


class ProxyEntity(Model):
    ip = CharField()
    port = IntegerField()
    full_ip = CharField()
    is_https = BooleanField()
    is_anonymous = BooleanField()
    country = CharField()
    city = CharField()
    location = CharField()

    class Meta:
        database = db
        # indexes = (
        #     # create a unique on from/to/date
        #     (('city', 'category', 'subcategory', "area"), True),
        # )

    def __str__(self):
        return f"{self.ip}:{self.port} is_https:{self.is_https} is_anonymous:{self.is_anonymous}"
