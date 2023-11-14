
def format_response(users: list) -> dict:
    Iuser = dict()
    KEYS = ("id","username","password","email")

    for pos, key in enumerate(KEYS):
        Iuser[key] = users[pos]

    return Iuser.copy()
