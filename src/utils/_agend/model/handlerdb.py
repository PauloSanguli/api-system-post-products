from ...models import connectMySQL
from .querys import selectPosts
from .querys import deletePostAgend
from ...models.accountpost import handlerPosts as Ihandler




class handlerDB:
    def __init__(self):
        objConnection = connectMySQL()
        response = objConnection.connect()
        if response["status"]:
            self.db = response["connection"]
            self.cursor = self.db.cursor()
        else:
            return {
                "msg": "dont connected",
                "status": False
            }

    def CreatePostArticle(self, user_id, title_article, content_text, price):
        post = Ihandler()
        response_create = post.createPost(user_id, title_article, content_text, price)

    def deleteAgendPost(self, user_id: int, post_id: int) -> dict:
        _SQL = deletePostAgend(user_id, post_id)
        self.cursor.execute(_SQL["statement"], _SQL["args"])
        self.db.commit()

    def select_all(self):
        try:
            _SQL = selectPosts()
            self.cursor.execute(_SQL["statement"])
            data = self.cursor.fetchall()
        except Exception as error:
            return {
                "msg": "error to fetch datas",
                "status": False
            }
        else:
            return {
                "msg": "datas selected",
                "status": True,
                "datas": data
            }
