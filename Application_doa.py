from sql_connection import get_sql_connection

def get_user(connection):
    cursor = connection.cursor()


    query = ("SELECT account_number , Name , Balance From Users")


    cursor.execute(query)

    for (account_number , Name , Balance) in cursor:
        print(account_number ,Name , Balance)

    cursor.close()
    
    
def add_users(connection):
    cursor = connection.cursor()

    add_user = ("INSERT INTO Users"
                "(Name , Balance)"
                "VALUES (%s, %s)")
            
        
    data_user = ("Dhruvin", "4444")    
    cursor.execute(add_user , data_user)

    connection.commit()

    cursor.close()
    

if __name__ == '__main__':
    connection =  get_sql_connection()
    get_user(connection) 
    add_users(connection)