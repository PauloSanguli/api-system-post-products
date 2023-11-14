import datetime
from .model.handlerdb import handlerDB as Ihandler




def getDateTimeNow() -> any:
    date = dict()

    date['year'] = int(datetime.date.today().year)
    date['month'] = int(datetime.date.today().month)
    date['day'] = int(datetime.date.today().day)

    return date.copy()


def verifyDatesToRemoveAgend(date: str):
    dateSystem = getDateTimeNow()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])

    if dateSystem['year'] == year or dateSystem['year'] > year:
        if dateSystem['month'] == month or dateSystem['month'] > month:
            if dateSystem['day'] == day or dateSystem['day'] > day:
                return True

    return False


def selectDates():
    db = Ihandler()
    response = db.select_all()
    datas = response["datas"]

    for post in datas:
        retire = verifyDatesToRemoveAgend(str(post[8]))
        if retire:
            user_id = post[0]
            title_article = post[2]
            content_text = post[3]
            price = post[6]
            post_id = post[1]

            db.CreatePostArticle(user_id, title_article, content_text, price)
            db.deleteAgendPost(user_id, post_id)
