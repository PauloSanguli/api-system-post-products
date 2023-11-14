
class querysMySQL():
    myType = dict
    def select_by_Email(email: str) -> myType:
        _SQL = dict()

        _SQL["statement"] = """SELECT * FROM `account_admin` WHERE `email` = (%s)"""
        _SQL["args"] = (email)

        return _SQL.copy()

    def selectAll() -> myType:
        _SQL = dict()
        _SQL["statement"] = """SELECT * FROM `account_admin`"""

        return _SQL.copy()
