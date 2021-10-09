from flask_app.config.mysqlconnection import connectToMySQL
db_name = 'recipes_schema'
from flask import flash

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_minutes = data['under_30_minutes']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "select * from recipes;"
        results = connectToMySQL(db_name).query_db(query)
        recipes = []
        for result in results:
            recipes.append(cls(result))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "select * from recipes where id = %(id)s;;"
        result = connectToMySQL(db_name).query_db(query, data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = """
        insert into recipes 
        (name, description, under_30_minutes, instructions, date_made, user_id, created_at, updated_at) 
        values 
        (%(name)s, %(description)s, %(under_30_minutes)s, %(instructions)s, %(date_made)s, %(user_id)s, now(), now());
        """
        # comes back as the new row id
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "delete from recipes where id = %(id)s;"
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        update recipes
        set name = %(name)s, description = %(description)%, under_30_minutes = %(under_30_minutes)s,
        instructions = %(instructions)s, date_made = %(date_made)s,  updated_at = now()
        where id = %(id)s;
        """
        return connectToMySQL(db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Name must be at least 3 characters long.', 'recipe')
            is_valid = False
        if len(recipe['description']) < 3:
            flash('Description must be at least 3 characters long.', 'recipe')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Instructions must be at least 3 characters long.', 'recipe')
            is_valid = False
        if not recipe['date_made']:
            flash('Date Made can not be empty.', 'recipe')
            is_valid = False
        if not recipe['under_30_minutes']:
            flash('Under 30 Minutes can not be empty.', 'recipe')
            is_valid = False
        return is_valid