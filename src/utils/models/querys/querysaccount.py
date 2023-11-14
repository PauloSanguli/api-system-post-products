
class querysMySQL():
    myType = dict
    def __init__(self):
        ...

    def insert(username: str, password: str, email: str) -> myType:
        SQL = dict()

        SQL["statement"] = """INSERT INTO `account_admin`(`username`, `password`, `email`) VALUES(%s, %s, %s)"""
        SQL["args"] = (username, password, email)

        return SQL.copy()

    def select_all() -> myType:
        _SQL = dict()

        _SQL["statement"] = """SELECT * FROM `account_admin`"""

        return _SQL.copy()

    def selectIdByEmail(email: str, username: str) -> myType:
        _SQL = dict()
        _SQL["statement"] = """SELECT `id` FROM `account_admin` WHERE `email` = %s and `username` = %s"""
        _SQL["args"] = (email, username)

    def selectIdByEmail_(email: str) -> myType:
        _SQL = dict()
        _SQL["statement"] = """SELECT `id` FROM `account_admin` WHERE `email` = %s"""
        _SQL["args"] = (email)

        return _SQL.copy()

    def selectPwdById(id: str) -> myType:
        _SQL = dict()
        _SQL["statement"] = """SELECT `password` FROM `account_admin` WHERE `id` = %s"""
        _SQL["args"] = (id)

        return _SQL.copy()

    def insertInfo(userid: int, username: str, password: str, email: str) -> myType:
        SQL = dict()

        SQL["statement"] = """INSERT INTO `account_info`(`user_id`,`username`, `password`, `email`) VALUES(%s, %s, %s, %s)"""
        SQL["args"] = (userid, username, password, email)

        return SQL.copy()

        return _SQL.copy()

    def selectById(id: int) -> dict:
        _SQL = dict()
        _SQL["statement"] = """SELECT * FROM `account_admin` WHERE `id` = %s"""
        _SQL["args"] = (id)

        return _SQL.copy()

    def selectAllByEmail(email: str) -> myType:
        _SQL = dict()

        _SQL["statement"] = """SELECT * FROM `account_admin` WHERE `email` = %s"""
        _SQL["args"] = (email)

        return _SQL.copy()