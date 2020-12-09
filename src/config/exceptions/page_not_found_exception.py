class PageNotFoundException(Exception):

    def __init__(self, message=None, url=None, status_code=None):
        if message:
            message = 'The page was not found, sorry :('
        self.url = url
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
