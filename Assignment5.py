students = { "Ayush" :80 , "Lakshay ": 50 , "Aarush" : 85 , "Sahej" : 56}
name = str(input("Enter your name :"))
if name in students:
    print(f"{name} marks : {students[name]}")
else :
    print(f"{name} not found")
