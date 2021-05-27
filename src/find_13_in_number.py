#!/usr/bin/python3

def find_13_by_math(number):
    # It is pretty complex to solve this like below, with just math functions.
    # It would have been much easier to convert the input to string and then
    # use the find_13_by_string_conversion function instead

    found = False
    pos = 0

    # Get magnitude of number, eg if number=23018 magnitude=10000
    magnitude = 1
    while magnitude < number/10:
        magnitude *= 10

    while not found and number >= 13:
        # Get the remaining number without the first two digits
        # 40004 will become 4.
        # 12345 will become 345.
        tmp = number % (magnitude/10)

        # Create a number starting with 13 and the same magnitude
        # as the number we are looking at and then add the remainings
        # from the last calc.
        compareNumber = (13 * (magnitude/10)) + tmp

        # If the created number is the same as the number we are
        # looking for, we have found what we want.
        if compareNumber == number:
            found = True
        else:
            number = number % magnitude # Removes at least one digit from front
            magnitude = magnitude / 10
            pos += 1
    if found:
        return pos
    return None

def find_13_by_string_conversion(number):
    pos = 0
    found_pos = None
    number_as_string = str(number)

    while pos < len(number_as_string):
        if number_as_string[pos] == '1':
            pos += 1
            if pos < len(number_as_string) and number_as_string[pos] == '3':
                found_pos = pos-1
                break
        pos += 1
    return found_pos


#numbers = [413044, 18939213094, 26, 9, 13940, 4839813, 241345, 40013]
#
#for number in numbers:
#    print(f"Number {number}: {find_13_by_math(number)}, {find_13_by_string_conversion(number)}")

