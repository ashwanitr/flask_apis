import sqlite3
from db import db
class ItemModel(db.Model):
    # TABLE_NAME = 'items'
    __tablename__='items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(73))
    price = db.Column(db.Float(precision=2))
    

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name, "price":self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(row[0],row[1])


    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=ItemModel.TABLE_NAME)
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()


    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=ItemModel.TABLE_NAME)
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()
