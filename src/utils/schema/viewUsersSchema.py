'''
DICT = {
  "response": {
    "datas": [
      [
        123456789,
        "Paulo Sanguli",
        "$2b$12$laVTmo8dK1yfjGC0ug0/Bu0sqI9h1qBcoAFtUxRd0zdE/qE6aUpSy",
        "paulosanguli@gmail.com"
      ],
       [
        123456789,
        "Paulo Sanguli",
        "$2b$12$laVTmo8dK1yfjGC0ug0/Bu0sqI9h1qBcoAFtUxRd0zdE/qE6aUpSy",
        "paulosanguli@gmail.com"
      ],
       [
        123456789,
        "Paulo Sanguli",
        "$2b$12$laVTmo8dK1yfjGC0ug0/Bu0sqI9h1qBcoAFtUxRd0zdE/qE6aUpSy",
        "paulosanguli@gmail.com"
      ]
    ],
    "msg": "datas selected",
    "status": True
  }
}
datas = DICT["response"]["datas"]
'''

def format_response(users: list) -> dict:
    Iresponse = list()
    KEYS = ("id","username","password","email")

    for user in users:
        Iuser = dict()
        for pos, key in enumerate(KEYS):
            Iuser[key] = user[pos]
        Iresponse.append(Iuser.copy())

    return Iresponse.copy()
