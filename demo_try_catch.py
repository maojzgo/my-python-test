#异常捕获
#日志打印
import logging
def f():
    try:
        a=1/0
    except ZeroDivisionError as e:
        logging.error(e)
    finally:
        logging.info("finally")

logging.basicConfig(level=logging.INFO)
f()
logging.info("abc")