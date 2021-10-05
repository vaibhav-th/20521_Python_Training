def validate(a, b):
    if check_string(a) and check_string(b):
        if check_pass(b):
            return True
        else:
            return False
    return False


def check_string(x):
    if type(x) == str:
        return True
    else:
        return False


def check_pass(y):
    special = ['$', '@', '#', '%']
    val = True

    if len(y) < 8:
        val = False

    if not any(char.isdigit() for char in y):
        val = False

    if not any(char.isupper() for char in y):
        val = False

    if not any(char in special for char in y):
        val = False

    return val