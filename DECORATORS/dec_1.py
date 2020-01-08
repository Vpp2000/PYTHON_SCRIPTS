def outer_function(msg):

	def inner_function():
		print(f"Message: {msg}")

	return inner_function


hi_var=outer_function('hi')
bye_var=outer_function('bye')

hi_var()
bye_var()