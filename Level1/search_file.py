import os
import time
class SearchFile:
    def __init__(self):
        pass

    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename#instanvce data
        self.filepath=filepath
        for root,dir,file in os.walk(filepath):
            if filename in file:
                #files.append(filename)
                files.append(os.path.join(root,filename)) #exactpath location
        return files
'''
if __name__=='__main__':
    #obj=SearchFile()
    #print(obj.find_file('demo.txt','c:\demo'))


    #searchengine
    st=time.time()
    obj=SearchFile()
    print(obj.find_file('file.txt','C:\\'))
    et=time.time()
    print(et-st)
'''