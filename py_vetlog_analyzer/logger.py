import logging


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    def info(self, message, args=None):
        self.logger.info(message) if args == None else self.logger.info(message, args)
