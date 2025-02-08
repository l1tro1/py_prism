from logging import getLogger

logger = getLogger(__name__)

def logged(func):
  def wrapper(*args, **kwargs):
    try:
      qualfuncname = f"{func.__qualname__}"
      logger.info(f"started {qualfuncname}, params: {args} and {kwargs}")
      return func(*args, **kwargs)
    except Exception as e:
      logger.exception(e)
  return wrapper