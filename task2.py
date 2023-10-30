
a={
    "name": "Jane",
    "surname": "Thomson",
    "age": 28,
    "isMarried": True
}

b=int(input("Daxil edin 1 Keys 2 Values - "))

if b==1:
    print(a.keys())
elif b==2:
    print(a.values())
elif b=="":
    print("Melumat daxil etmediniz")