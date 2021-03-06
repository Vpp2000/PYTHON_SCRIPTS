from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename=f'{orig_func.__name__}.log',level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args,**kwargs):  ## adding extra functionality
		logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
		return orig_func(*args,**kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args,**kwargs): ## adding extra functionality
		t1 = time.time()
		time.sleep(1)
		result = orig_func(*args,**kwargs)
		t2 = time.time()-t1
		print(f'{orig_func.__name__} ran in {t2} sec')
		return result

	return wrapper


@my_logger
@my_timer
def display_info(name,age):
	print(f'display_info ran with arguments {name} and {age}')

"""
modified_display = my_logger(display_info)
modified_display('Gusfraba',23)
"""
display_info('Hans',38)