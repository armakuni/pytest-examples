def fizzbuzz(input):
    if type(input) is not int:
        raise Exception(f"'{input}' is not a number")
    if input % 15 == 0:
        return "fizzbuzz"
    if input % 5 == 0:
        return "buzz"
    if input % 3 == 0:
        return "fizz"
    return str(input)
