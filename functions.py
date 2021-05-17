def get_sum(one: str, two: str, delimiter='&'):
    one = str(one).capitalize()
    two = str(two).capitalize()
    result = one + ' ' + delimiter + ' ' + two
    return result


if __name__ == '__main__':
    example_variable = get_sum('Learn', 'python')
    print(example_variable)
