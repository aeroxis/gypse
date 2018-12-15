from urllib.parse import urlparse

class URL(object):

    def __init__(self, url):

        parsed = urlparse(url)
        self.scheme = parsed.scheme
        self.netloc = parsed.netloc
        self.path = parsed.path
        self.params = parsed.params
        self.query = parsed.query
        self.fragment = parsed.fragment
        self.url = url
        