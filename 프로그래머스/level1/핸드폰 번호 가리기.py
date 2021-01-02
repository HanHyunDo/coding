def solution(phone_number):
    a = phone_number[-4:]
    b = len(phone_number[:-4]) * '*'
    return f'{b}{a}'

