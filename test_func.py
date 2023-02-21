def is_float(str_val):
try:
# If the string isn't a float float() will throw a
# ValueError
float(str_val)
# If there is a value you want to return use return
return True
except ValueError:
return False