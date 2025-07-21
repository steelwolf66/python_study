from datetime import datetime

print(datetime.now())
print(datetime.now().year)
print(type(datetime.now().month))

timestamp = datetime.now().timestamp()
print(timestamp)
print(type(timestamp))