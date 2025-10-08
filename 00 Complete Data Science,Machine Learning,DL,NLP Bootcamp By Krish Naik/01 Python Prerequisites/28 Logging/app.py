import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Create a custom logger
logger = logging.getLogger("ArithmeticAPP")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a} to get {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b} to get {result}")
    except ZeroDivisionError:
        logger.error(f"Attempted to divide by zero")
        result = None
    
    
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
divide(10, 0)
