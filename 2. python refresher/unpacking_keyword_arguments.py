# def named(**kwargs):
# 	print(kwargs)

# named(name = 'Bob', age = 25)


def named(name, age):
	print(name, age)

details = {'name': 'Bob', 'age': 25}

named(**details)

def print_nicely(**kwargs):
	named(**kwargs)
	for arg, value in kwargs.items():
		print(f"{arg}: {value}")

print_nicely(name='Bob', age=25)   