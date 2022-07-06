import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This Field cannot be left Blank!"
    ) #* If you have a HTML Form, you can use this RequestParser to go through the Form Fields

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row: # if row is found
            return {"item":{"name": row[0], "price": row[1]}}
    
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item["price"], item["name"]))

        connection.commit()
        connection.close()


    #^ NOTE     GET METHOD
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {"message": "Item Not Found"}, 404 # else
    

    #^ NOTE     POST METHOD
    def post(self, name):
        if self.find_by_name(name):
            return {"message": "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {"name": name, "price":data["price"]}

        try:
            self.insert(item)
        except:
            return {"message": "An Error Occured while inserting the New Item"}, 500 # Internal Server Error
        return item, 201


    #^ NOTE     DELETE METHOD
    def delete(self, name):
        item = Item.find_by_name(name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        if item:
            return {"message": "Item Deleted"}
        else:
            return {"message": "Item Not Found"}, 404
    

    #^ NOTE     PUT METHOD
    def put(self, name): #* For both Posting and Updating an Item
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {"name": name, "price": data["price"]}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An Error Occured while inserting the Item"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An Error Occured while Updating the Item"}, 500
        return updated_item



class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})

        connection.close()
        return {"items": items}