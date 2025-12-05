def validate_id():
    def validator(check_scale):
        result = 0
        for num in range(10):
            result += check_scale[num] * int(isikukood[num])
        return result
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    if validator(chk1) % 11 == int(isikukood[-1]):
        print('ID is valid')
    elif validator(chk1) % 11 == 10:
        if validator(chk2) % 11 == int(isikukood[-1]):
            print('ID is valid')
        else:
            print('ID is not valid')
    else:
        print('ID is not valid')


isikukood = '38803160272'

validate_id()