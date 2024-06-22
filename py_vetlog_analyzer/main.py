from py_vetlog_analyzer.database_filter import *


def find():
    Filter().filter_usernames()


def suggest():
    Filter().suspicious_usernames()
