calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str):
    count_calls()
    work_tuple = (len(str), str.upper(), str.lower())
    return work_tuple


def is_contains(text, text_list):
    count_calls()
    text_list = list(map(str.lower, text_list))
    if text.lower() in text_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
