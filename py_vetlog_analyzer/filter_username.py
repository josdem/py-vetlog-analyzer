def filter_username(username):
    uppercase = 0
    for char in username:
        if char.isupper():
            uppercase += 1
    result = uppercase / len(username)        
    print(result)        
    return uppercase / len(username) < 0.5
