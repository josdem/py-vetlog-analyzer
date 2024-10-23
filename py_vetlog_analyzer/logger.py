import logging


class Logger:
    def __init__(self, name):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.log.addHandler(self.console_handler)

    def info(self, message, args=None):
        self.log.info(message) if args == None else self.log.info(message, args)
