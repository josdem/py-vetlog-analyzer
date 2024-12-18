def filter_username(username):
    if username.isupper():
        return True
    if len(username) < 8:
        return True
    uppercase = 0
    for char in username:
        if char.isupper():
            uppercase += 1
    return uppercase / len(username) < 0.5
