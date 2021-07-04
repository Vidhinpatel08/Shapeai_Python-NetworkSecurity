#1
import hashlib

#2
given_str = b"Hello world"
given_str_2 = b"Hello world !!"

#3
md5_value = hashlib.md5(given_str)
md5_value_2 = hashlib.md5(given_str_2)

#4
print(md5_value.hexdigest())
print(md5_value_2.hexdigest())