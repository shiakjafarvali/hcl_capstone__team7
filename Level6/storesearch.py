import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except:
            print("Error while connecting to the database")

    def inser_data(self,filename):
        self.filename=filename
        #self.password=password
        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);"
        val=(self.filename)


        self.cur.execute(sql,(val,))

        self.connection.commit()


    def search(self):
        self.cur=self.connection.cursor()
        sql='select * from files limit 0,10'
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data


'''
def inser_data(self, username,password):
        self.username=username
        self.password=password
        self.cur=self.connection.cursor()
        sql="insert into user(username,passwd) values(%s,%s);"
        val=(self.username,self.password)

        self.cur.execute(sql,(val))

        self.connection.commit()

    def inser_data(self,filename):
        self.filename = filename
        #self.password = password
        self.cur = self.connection.cursor()
        sql = "insert into files(filename) values(%s);"
        val = (self.filename)

        self.cur.execute(sql, (val,))

        self.connection.commit()

    '''

dbobj=Mysql_DBaccess('localhost','root','Root','searchfile')
print(dbobj)
dbobj.inser_data('C://demo//demo.txt')
#dbobj.inser_data('jafar','jafar')