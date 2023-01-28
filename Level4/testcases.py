import pytest
from Level1.find_drives import SystemDriveFinder #class name
from Level1.search_file import SearchFile
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected =obj.find_drives() #['C','D']
        self.actual=['C']
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=SearchFile()
        d=obj.find_file('demo.txt','c:\demo')
        self.expected_filename=d[0]
        self.actual_res='c:\\demo\\demo.txt'
        assert self.expected_filename==self.actual_res
