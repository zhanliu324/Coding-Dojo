from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        insert into ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
        values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, now(), now())
        """
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)