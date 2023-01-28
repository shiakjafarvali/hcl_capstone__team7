import logging
logging.basicConfig(filename="mylogdetails.txt",level=logging.INFO,format="%(asctime)s%(levelname)s")
logging.info("A new log came")
try:
    n1=int(input("Enter the Number"))
    n2=int(input("Enter second Number"))
    print(n1/n2)
except ZeroDivisionError as e:
    print("Cannot divide with zero")
    logging.exception(e)
except ValueError as msg:
    print("value only")
    logging.exception(msg)
logging.info("Log is recorded")