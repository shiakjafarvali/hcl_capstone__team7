import mysql.connector
import os
import time
class SearchFile:
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

    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename#instanvce data
        self.filepath=filepath
        try:
            sql = """ select * from files where filename='{0}'""".format(filename)
            # sql = """ select * from files where filename like '%{0}'""".format(file)
            self.cur.execute(sql)
            row = self.cur.fetchone()
            if row == None:
                return 0
            else:
                return files.append(row)
        except:
            for root,dir,file in os.walk(filepath):
                if filename in file:
                    #files.append(filename)
                    files.append(os.path.join(root,filename)) #exactpath location
            return files
if __name__=='__main__':
    st = time.time()
    obj=SearchFile('localhost','root','Root','searchfile')
    print(obj.find_file('file.txt','c:\hcl'))
    et = time.time()
    print(et-st)
    st1 = time.time()
    print(obj.find_file('demo.txt', 'c:\demo'))
    et1 = time.time()
    print(et1 - st1)

'''
    #searchengine
    st=time.time()
    obj=SearchFile()
    print(obj.find_file('file.txt','C:\\'))
    et=time.time()
    print(et-st)
'''