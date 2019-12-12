from models.link import *

class Response:
    def __init__(self, raw_response):
        self.raw_response = raw_response

    def items(self):
        return list(map(lambda data: Link(data), self.raw_response.json()['data']['children']))

    def linkify(self, data):
        return Link(data)
