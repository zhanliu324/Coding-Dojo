from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "select * from dojos"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def save(cls,data):
        query = "insert into dojos (name, created_at, updated_at) values (%(name)s, now(), now())"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
        select *
        from dojos
        left join ninjas on dojos.id = ninjas.dojo_id
        where dojos.id = %(id)s
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'dojo_id': row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja))
        return dojo