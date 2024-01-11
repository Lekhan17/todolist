import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host' : 'localhost',
    'database': 'todolist',
}
class Model():
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
    

    def addingTask(self, tasks):
        cursor = self.conn.cursor()
        sql = "INSERT INTO addtask (tasks) VALUES(%s)"
        cursor.execute(sql,(tasks,))
        self.conn.commit()
        cursor.close()
        return  {'status':'Success', 'msg': 'Data is sent'}
        
    def displayTask(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM addtask"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    # def deleteTask(self, id):
    #     cursor = self.conn.cursor()
    #     sql = "DELETE FROM addtask WHERE  id=%s"
    #     cursor.execute(sql,[id])
    #     self.conn.commit()
    #     cursor.close()


        


