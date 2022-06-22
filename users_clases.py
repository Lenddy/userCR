# you need to import my from mysqlconnection import connectToMySQL so you can run you data base
from mysqlconnection import connectToMySQL


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# all of the methods the we defin must be @classmethods
    @classmethod
    def get_all_users(cls):
        query = "select * from users;"
# this alway will be returning a list of dictionarys
        result = connectToMySQL("users_schema").query_db(query)
        print(result)
        all_users = []
# we need a for loop here that is going to push/append all the users to a list that we have
        for row in result:
            all_users.append(cls(row))
        return all_users

    @classmethod
    def add_new_user(cls, data):
#you need to add this syntax %()s because you dont want the same user to be added
        query = "insert into users (first_name,last_name,email) values(%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL("users_schema").query_db(query, data)
