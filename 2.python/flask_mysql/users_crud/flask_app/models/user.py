# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the user table from our database

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "select * from users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for result in results:
            users.append(cls(result))
        return users

    @classmethod
    def save(cls, data):
        query = "insert into users (first_name, last_name, email, created_at, updated_at) values (%(first_name)s, %(last_name)s, %(email)s, now(), now());"
        # comes back as the new row id
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "delete from users where id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "update users set first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "select * from users where id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return cls(result[0])