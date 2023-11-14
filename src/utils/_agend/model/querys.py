

def selectPosts() -> dict:
    _SQL = dict()
    _SQL["statement"] = """SELECT * FROM `account_post_agend`"""

    return _SQL.copy()

def deletePostAgend(user_id: int, post_id: int) -> dict:
    _SQL = dict()
    _SQL["statement"] = """DELETE FROM `account_post_agend` WHERE `user_id` = %s AND `post_id` = %s"""
    _SQL["args"] = (user_id, post_id)

    return _SQL.copy()