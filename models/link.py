class Link:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def data(self):
        return self.raw_data['data']

    def downs(self):
        return self.data()['downs']

    def name(self):
        return self.data()['name']

    def score(self):
        return self.data()['score']

    def subreddit(self):
        return self.data()['subreddit']

    def title(self):
        return self.data()['title']

    def ups(self):
        return self.data()['ups']
