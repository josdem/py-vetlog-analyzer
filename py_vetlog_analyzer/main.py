from py_vetlog_analyzer.database_filter import Filter
from py_vetlog_analyzer.database_filter_pets import PetFilter


def find():
    Filter().filter_usernames()


def suggest():
    Filter().suspicious_usernames()


def vaccines():
    PetFilter().filtering_pets()
