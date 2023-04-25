
class BaseException_(Exception):
    def __init__(self, message, exception=None, status=400, *args):
        super().__init__(args)
        self.message = message
        self.status = status
        self.exception = exception