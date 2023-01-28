import pytest
def test_demo1():
    a=10
    b=20
    assert a!=b #gives true or false
def test_demo2():
    name='HCL'
    text='HCL is located all over India'
    assert name in text #hcl is there in text or not

#to run all test go to commond promot terminal cd level4 and pytest and pytest pytest_demo.py -v gives detailed
#pytest pytest_demo.py -ra (flags in pytest)

