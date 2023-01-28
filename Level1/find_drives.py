import os #to communicate underlined os
class SystemDriveFinder:
    def __init__(self):
        pass

    def find_drives(self): #instance method belong to obj
        #write the logic to get all the drives in the system (Active or Inactive)
        print("This is the find drives method of System Drive Finder class")

        drives=[] #storing all drives
        for x in range(65,91):
            if os.path.exists(chr(x)+':'):
                drives.append(chr(x)) #appending to the list

        return drives
'''
if __name__ == "__main__":
    obj=SystemDriveFinder()
    print(obj.find_drives())
'''