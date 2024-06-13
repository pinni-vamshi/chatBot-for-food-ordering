import pymysql
global cnx

cnx = pymysql.connect(
    host="localhost",
    user="root",
    password="Pinni1598@",
    database="pandeyji_eatery")

# Function to call the MySQL stored procedure and insert an order item
def get_item_id(food_item):
    print("get item id fucntion is called:", food_item)
    try:
        cursor = cnx.cursor()
        query = f"SELECT item_id FROM pandeyji_eatery.food_items WHERE name = %s"
        cursor.execute(query, (food_item,))
        row = cursor.fetchone()
        print("row: ", row)
        cursor.close()
        if row:
            return row[0]
        else:
            return None
    except pymysql.Error as err:
        print(f"Error getting item ID: {err}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
#
#
def get_price( food_items):
    cursor = cnx.cursor()
    query = "SELECT price FROM pandeyji_eatery.food_items WHERE name = %s"
    cursor.execute(query , (food_items))
    cnx.commit()
    result = cursor.fetchone()[0]
    print("food_item price: ", result)
    cursor.close()

    return result




def insert_order_item(order_id, item_id , quantity , total_price):
    print("order id :", order_id)
    print("item id :", item_id)
    print("quantity :", quantity)
    print("price: ", total_price)
    try:
        cursor = cnx.cursor()
        # Calling the stored procedure
        insert_query = "INSERT INTO pandeyji_eatery.orders (order_id,item_id, quantity, total_price) VALUES (%s, %s , %s, %s)"
        cursor.execute(insert_query, (order_id,item_id, quantity, total_price))
        cnx.commit()
        cursor.close()
        print("Order item inserted successfully!")
        return 1
    except pymysql.Error as err:
        print(f"Error inserting order item: {err}")
        cnx.rollback()
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        cnx.rollback()
        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))
    cnx.commit()
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    print("get total order price: ", result)
    return result

def get_next_order_id():
    cursor = cnx.cursor()
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    if result is None:
        return 1
    else:
        return result + 1

def get_order_status(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())
