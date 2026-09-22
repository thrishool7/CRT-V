'''
a = 10
b = 5.6
c = "Krishna"
d = [1,2,3,4,5,6]
e = (1,2,3,4,5,6)
f = {1,2,3,4,5,6}
g = {"name":"Krishna"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

'''
'''
isinstance() function is used to check if an object is an instance of a class or a subclass thereof. It returns True if the object is an instance of the specified class or a subclass, and False otherwise.
Syntax: isinstance(object, classinfo)
 
'''
a = 10
b = 5.6
c = "Krishna"
d = [1,2,3,4,5,6]
e = (1,2,3,4,5,6)
f = {1,2,3,4,5,6}
g = {"name":"Krishna"}
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))
print(isinstance(e, tuple))
print(isinstance(f, set))
print(isinstance(g, dict))



