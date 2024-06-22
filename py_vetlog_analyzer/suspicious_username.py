def is_suspicious_username(username: str) -> bool:
    uppercase = 0
    for char in username:
        if char.isupper():
            uppercase += 1
    return 0.2 < uppercase / len(username) <= 0.5
