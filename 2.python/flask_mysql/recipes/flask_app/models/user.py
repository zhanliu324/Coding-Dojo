from flask_app.config.mysqlconnection import connectToMySQL
db_name = 'recipes_schema'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def get_all(cls):
    #     query = "select * from users;"
    #     results = connectToMySQL('users_schema').query_db(query)
    #     users = []
    #     for result in results:
    #         users.append(cls(result))
    #     return users

    @classmethod
    def save(cls, data):
        query = """
        insert into users 
        (first_name, last_name, email, password, created_at, updated_at) 
        values 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s, now(), now());
        """
        # comes back as the new row id
        return connectToMySQL(db_name).query_db(query, data)
        

    # @classmethod
    # def delete(cls, data):
    #     query = "delete from users where id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = "update users set first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "select * from users where id = %(id)s;"
        result = connectToMySQL(db_name).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where email = %(email)s;"
        result = connectToMySQL(db_name).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", 'register')
            is_valid = False
        if User.get_by_email(user):
            flash('Email already existed. Please use another one.', 'register')
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters.', 'register')
            is_valid = False
        if not user['first_name'].isalpha():
            flash('First name must be letters only.', 'register')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters.', 'register')
            is_valid = False
        if not user['last_name'].isalpha():
            flash('Last name must be letters only.', 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", 'register')
            is_valid = False
        if not re.search('[0-9]', user['password']):
            flash("Password must have at least 1 number.", 'register')
            is_valid = False
        if not re.search('[A-Z]', user['password']):
            flash("Password must have at least 1 uppercase letter.", 'register')
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Password don't match.", 'register')
            is_valid = False
        return is_valid

