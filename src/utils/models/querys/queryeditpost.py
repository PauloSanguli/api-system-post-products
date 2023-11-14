
class querysMySQL():
    myType = dict
 
    
    def update_title(user_id: int, post_id: int, new: str) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `posts` SET `title_article` = %s WHERE `user_id` = %s and `post_id` = %s"""
        _SQL["args"] = (new, user_id, post_id)

        return _SQL.copy()


    def update_content(user_id: int, post_id: int, new: str) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `posts` SET `content_text` = %s WHERE `user_id` = %s and `post_id` = %s"""
        _SQL["args"] = (new, user_id, post_id)

        return _SQL.copy()


    def update_img(user_id: int, post_id: int, new: any) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `posts` SET `content_img` = %s WHERE `user_id` = %s and `post_id` = %s"""
        _SQL["args"] = (new, user_id, post_id)

        return _SQL.copy()


    def update_date(user_id: int, post_id: int, new: str) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `posts` SET `date_posted` = %s WHERE `user_id` = %s and `post_id` = %s"""
        _SQL["args"] = (new, user_id, post_id)

        return _SQL.copy()

    
    def update_price(user_id: int, post_id: int, new: float) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `posts` SET `price` = %s WHERE `user_id` = %s and `post_id` = %s"""
        _SQL["args"] = (new, user_id, post_id)

        return _SQL.copy()
    