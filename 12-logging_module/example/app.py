import logging

## configuring logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('ArithematicApp')

def add(a,b):
    res=a+b
    logger.debug(f"Adding {a} + {b} = {res}")
    return res

def subtract(a,b):
    res=a-b
    logger.debug(f"subtraction {a} - {b} = {res}")
    return res

def multiply(a,b):
    res=a*b
    logger.debug(f"multiply {a} * {b} = {res}")
    return res

def divide(a,b):
    try:
        res=a/b
        logger.debug(f"dividing {a} / {b} = {res}")
        return res
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,15)
subtract(15,10)
multiply(2,5)
divide(20,0)
divide(35,6)