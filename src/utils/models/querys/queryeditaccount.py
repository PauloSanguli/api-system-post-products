from typing import Type



class querysMySQL():
    myType = dict
 
    def select_all(user_id: int) -> myType:
        _SQL = dict()

        _SQL["statement"] = """SELECT * FROM `account_info` WHERE `user_id` = %s"""
        _SQL["args"] = (user_id)

        return _SQL.copy()


    def update_name(user_id: int, new: str) -> myType:
        _SQL = dict()
        _SQLmany = list()

        _SQL["statement"] = """UPDATE `account_info` SET `username` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (new, user_id)

        _SQLmany.append(_SQL.copy())

        _SQL["statement"] = """UPDATE `account_admin` SET `username` = %s WHERE `id` = %s"""
        _SQL["args"] = (new, user_id)

        _SQLmany.append(_SQL.copy())

        return _SQLmany


    def update_email(user_id: int, new: str) -> myType:
        _SQL = dict()
        _SQLmany = list()

        _SQL["statement"] = """UPDATE `account_info` SET `email` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (new, user_id)

        _SQLmany.append(_SQL.copy())

        _SQL["statement"] = """UPDATE `account_admin` SET `email` = %s WHERE `id` = %s"""
        _SQL["args"] = (new, user_id)
        
        _SQLmany.append(_SQL.copy())

        return _SQLmany


    def update_date(user_id: int, new: any) -> myType:
        _SQL = dict()
        _SQLmany = list()

        _SQL["statement"] = """UPDATE `account_info` SET `date_born` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (new, user_id)

        return _SQL.copy()
    

    def update_phone(user_id: int, new: any) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `account_info` SET `phone_number` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (new, user_id)

        return _SQL.copy()

    
    def update_img(user_id: int, new: any) -> myType:
        _SQL = dict()

        _SQL["statement"] = """UPDATE `account_info` SET `img_perfil` = %s WHERE `user_id` = %s"""
        _SQL["args"] = (new, user_id)

        return _SQL.copy()

    def viewData(user_id: int) -> dict:
        _SQL = dict()

        _SQL["statement"] = """SELECT * FROM `account_info` WHERE `user_id` = %s"""
        _SQL["args"] = (user_id)

        return _SQL.copy()
        
    def update_password(user_id: int, new: str) -> myType:
        _SQL = dict()
        _SQL["statement"] = "UPDATE `account_admin` SET `password` = %s WHERE `id` = %s"
        _SQL["args"] = (new, user_id)

        return _SQL.copy()