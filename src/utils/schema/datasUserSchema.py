'''
DICT = {
  "response": {
    "datas": [
      123456789,
      "$2b$12$laVTmo8dK1yfjGC0ug0/Bu0",
      "Paulo Sanguli",
      "paulosanguli@gmail.com",
      None,
      None,
      "Fri, 08 Sep 2023 14:07:15 GMT",
      None,
      0
    ],
    "msg": "datas selected",
    "status": True
  }
}
datas = DICT["response"]["datas"]
'''

def format_response(values: list) -> dict:
    Iresponse = dict()
    KEYS = ("id","password","username","email","dateborn","phone","date add","img","acess","number_posts")
        
    for pos,key in enumerate(KEYS):
        if key == 'acess':
            if values[pos]:
                Iresponse[key] = True
            else:
                Iresponse[key] = False
        else:
            Iresponse[key] = values[pos]

    return Iresponse.copy()
