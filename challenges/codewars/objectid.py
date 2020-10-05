import re
from datetime import datetime


class Mongo(object):
    @classmethod
    def is_valid(cls, s):
        return isinstance(s, str) and bool(re.match(r'[0-9a-f]{24}$', s))

    @classmethod
    def get_timestamp(cls, s):
        return cls.is_valid(s) and datetime.fromtimestamp(int(s[:8], 16))
