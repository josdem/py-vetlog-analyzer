from py_vetlog_analyzer.database_filter import Filter


def find():
    Filter().filter_usernames()


def suggest():
    Filter().suspicious_usernames()
