from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_and_order:

    DB = "cookies_schema"
    def __init__ (self, data):
        self.id = data['id']
        self.cookie_type = data['cookie_type']
        self.cust_name = data['cust_name']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #VALIDATION
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['cust_name']) < 2 :
            is_valid = False
            flash("Name must be at least 2 characters.")
        if len(order['cookie_type']) < 2:
            is_valid = False
            flash("Cookie Type must be at least 2 character")
        if int(order['number_of_boxes']) < 1:
            is_valid = False
            flash("Number of Boxes must be higher than 0")

        return is_valid


    # CREATE 

    @classmethod
    def save_order(cls, data):
        query = """
                INSERT INTO cookie_orders (cookie_type, cust_name, number_of_boxes)
                VALUES (%(cookie_type)s, %(cust_name)s, %(number_of_boxes)s)
                    """
        result = connectToMySQL(cls.DB).query_db(query, data)

    #READ 
    @classmethod
    def get_all_cookies(cls):
        query = """SELECT * FROM cookie_orders;"""
        results = connectToMySQL(cls.DB).query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def get_one_order(cls, order_id):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s"
        data = {'id': order_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])


    #UPDATE
    @classmethod
    def update_order(cls, updated_order):
        query = """
                UPDATE cookie_orders 
                SET cookie_type = %(cookie_type)s, cust_name = %(cust_name)s, number_of_boxes = %(number_of_boxes)s, updated_at = NOW()
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.DB).query_db(query, updated_order)
        return results