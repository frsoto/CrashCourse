bicycles = ['trek', 'cannondale', 'redline', 'specialized', 0.1]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # ultimo de la lista
print(bicycles[-2]) # ultimo de la lista
print(type(bicycles))
print(type(bicycles[0]))
print(type(bicycles[4])) # <class 'float'>

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
