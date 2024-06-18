def filter_username(username):
    uppercase = 0
    for char in username:
        if char.isupper():
            uppercase += 1
    return uppercase / len(username) < 0.5
