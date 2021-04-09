def spiralize(number):

    if number == 1:
        return_value = 1
    else:
        return_value = (
            (4 * number * number) - (6 * (number - 1)) + spiralize(number - 2)
        )
    return return_value

if __name__ == "__main__":
    print(spiralize(5))
    print(spiralize(501))
