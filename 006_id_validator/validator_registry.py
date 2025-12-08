def enter_id_code():
    
    while True:
        global id_code
        user_input = input('Please enter your national id: ')
        try:
            int(user_input)
            if len(user_input) != 11:
                raise UserWarning()
        except ValueError:
            print('Only numbers alowed')
            continue
        except UserWarning:
            print('Must be 11 digits long')
            continue
        else:
            id_code = user_input
            break


def get_gender():
    if int(id_code[0]) % 2 == 0:
        print('Female')
    else:
        print('Male')


def get_dob():
    century = ''
    if id_code[0] in '12':
        century = '18'
    elif id_code[0] in '34':
        century = '19'
    elif id_code[0] in '56':
        century = '20'
    elif id_code[0] in '78':
        century = '21'
    print(f'{id_code[5:7]}.{id_code[3:5]}.{century}{id_code[1:3]}')


def validate_id():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    def validator(check_weight):
        result = 0
        for num in range(10):
            result += int(id_code[num]) * check_weight[num]
        return result % 11
    
    # 38803160272
    
    if validator(chk1) == 10:
        if validator(chk2) == int(id_code[-1]):
            print('Code is valid 2')
        else:
            print('Code is invalid')
    elif validator(chk1) % 11 == int(id_code[-1]):
        print('Code is valid 1')
    else:
        print('Code is invalid')


def check_region():
    region_id = id_code[-4:-1]
    if region_id >= '001' and region_id <= '010':
        print('Kuressaare Hospital')
    elif int(region_id) in range(1, 11):
        print('Tartu University Women\'s Clinic')
    

def menu():
    registry = {
        '1': get_gender,
        '2': get_dob,
        '4': validate_id,
        '5': enter_id_code,
        '0': quit,
    }
    enter_id_code()
    while True:
        user_choice = input('1.Get gender\n' \
                            '2.Get date of birth\n' \
                            '3.Get region of birth\n' \
                            '4.Validate id\n' \
                            '5.Enter new id code\n' \
                            '0.Exit\n' \
                            '--> ')
        if user_choice in registry:
            registry[user_choice]()
        else:
            print('Choice is out of range')

id_code = ''

menu()