"""
class decorator_class(object):
	def __init__(self,original_function):
		self.original_function = original_function

	def __call__(self,*args,**kwargs):
		print(f"In the class, call method executed before {self.original_function.__name__}")
		return self.original_function(*args,**kwargs)
"""
def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		print(f"Another function was here: {original_function.__name__}")
		return original_function(*args,**kwargs)

	return wrapper_function

@decorator_function
def display():
	print('display function ran')

@decorator_function
def display_info(name,age):
	print(f'display_info ran with arguments {name} and {age}')


#decorated_display = decorator_function(display)
#decorated_display()	

display()
display_info('Nombre',55)
