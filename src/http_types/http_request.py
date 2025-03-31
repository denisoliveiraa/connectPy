class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None: 
        self.body = body 
        self.status_code = param