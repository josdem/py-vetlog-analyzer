from py_vetlog_analyzer.database_filter import Filter
from py_vetlog_analyzer.database_filter_pets import PetFilter


def flter_by_username():
    Filter().filter_users(10)


def flter_by_name():
    Filter().filter_users(11)


def flter_by_last_name():
    Filter().filter_users(12)


def suggest():
    Filter().suspicious_usernames()


def vaccines():
    PetFilter().filtering_pets()
