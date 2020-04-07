import eel
eel.init('web')

@eel.expose
def my_python_method(param1, param2):
	print(param1+param2)


eel.start('index.html')


