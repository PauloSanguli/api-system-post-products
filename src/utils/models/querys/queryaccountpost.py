from typing import Type



class querysMySQL():
    myType = dict
    def insert(user_id: int,title_article, content_text: str, price: float) -> myType:
        _SQL = dict()
        _SQL["statement"] = """INSERT INTO `posts`(`user_id`,`title_article`, `content_text`, `price`) VALUES (%s, %s, %s,  %s)"""
        _SQL["args"] = (user_id, title_article, content_text, price)

        return _SQL.copy()

    
    def insertPostAgend(user_id: int, title_article: str, content_text: str, price: float, date_agend) -> myType:
        _SQL = dict()
        _SQL["statement"] = """INSERT INTO `account_post_agend`(`user_id`, `title_article`, `content_text`, `price`, `date_agend`) VALUES(%s, %s, %s, %s, %s)"""
        _SQL["args"] = (user_id, title_article, content_text, price, date_agend)

        return _SQL.copy()


    def select_all(user_id: int) -> myType:
        _SQL = dict()
        _SQL["statement"] = """SELECT * FROM `posts` WHERE `user_id` = %s"""
        _SQL["args"] = (user_id)

        return _SQL.copy()



    def delete(user_id, post_id: int) -> myType:
        _SQL = dict()
        _SQL["statement"] = """DELETE FROM `posts` WHERE `post_id` = %s and `user_id` = %s"""
        _SQL["args"] = (post_id, user_id)

        return _SQL.copy()



    def update(user_id: int, post_id: int, showOrHidde: bool) -> myType:
        _SQL = dict()
        _SQL["statement"] = """UPDATE `posts` SET `show_post` = %s WHERE `post_id` = %s and `user_id` = %s"""
        _SQL["args"] = (showOrHidde, post_id, user_id)

        return _SQL.copy()
