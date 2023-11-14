

class querysMySQL():
    myType = dict
    def __init__(self):
        ...

    def update_by_id(id: int, acess: bool) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `account_info` SET `check_acess` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (acess, id)
    
        return _SQL.copy()