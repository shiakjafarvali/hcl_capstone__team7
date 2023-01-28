import mysql.connector
class SearchFileDB:

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        try:
            self.connection = mysql.connector.connect(host=self.host, database=self.db, user=self.user,
                                                      password=self.password)
        except:
            print("Error while connecting to the database")

    def searchDB(self,file):
        print(file)
        #sql='select * from filelog where filename ?;'
        self.f='filename'
        self.cur = self.connection.cursor()
        #data=(filename)
        sql=""" select * from files where filename='{0}'""".format(file)
        #sql = """ select * from files where filename like '%{0}'""".format(file)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==None:
            return 0
        else:
            return row

obj=SearchFileDB('localhost','root','Root','searchfile')
#obj.inser_data("demo")
print(obj.searchDB("C://demo//demo.txt"))