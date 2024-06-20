def get_correct_declension(number, one, two, five):
    number = abs(number) % 100
    if 11 <= number <= 19:
        return five
    number = number % 10
    if number == 1:
        return one
    if 2 <= number <= 4:
        return two
    return five


def get_ball_declension(score):
    return get_correct_declension(score, 'балл', 'балла', 'баллов')
