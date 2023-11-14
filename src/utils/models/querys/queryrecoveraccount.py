
def updatepwdById(id: int, password: str) -> dict:
    _SQL = dict()
    _SQL["statement"] = """UPDATE `account_admin` SET `password` = %s WHERE `id` = %s"""
    _SQL["args"] = (password, id)

    return _SQL.copy()