from sql_connection import get_sql_connection
import time 
def get_user(connection):
    cursor = connection.cursor()


    query = ("SELECT a.account_number , a.Name , a.Balance , a.branch_id ,b.branch_name From Users as a join branch as b on a.branch_id = b.branch_id")


    cursor.execute(query)

    for (account_number , Name , Balance , branch_id , branch_name ) in cursor:
        print(account_number ,Name , Balance , branch_id , branch_name)

    cursor.close()
    
    
def add_users(connection):
    cursor = connection.cursor()

    add_user = ("INSERT INTO Users"
                "(Name , Balance,branch_id)"
                "VALUES (%s, %s , %s)")
            
        
    data_user = ("Dhruvin1", "4444" ,1)    
    cursor.execute(add_user , data_user)

    connection.commit()

    cursor.close()
    
def delete_user(connection):
    cursor = connection.cursor()

    delete_user = "Delete from users where Name = %s"
    
    data_user = ("Dhruvin" , )

    cursor.execute(delete_user,data_user)

    connection.commit()

    cursor.close()







if __name__ == '__main__':
    connection =  get_sql_connection()
    get_user(connection)
    add_users(connection) 
    delete_user(connection)
    
    
    