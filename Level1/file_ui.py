from Level1.find_drives import SystemDriveFinder

filename=input("Enter the file name : ")
drive= input("Enter the drive : ")
obj=SystemDriveFinder()
print(obj.find_drives())
'''
filename=input("Enter the file name")
drive=input("Enter the Drive")
obj=SystemDriveFinder()
print(obj.find_drives(filename,drive))
'''