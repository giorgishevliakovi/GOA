ricxvi = int(input("შემოიყვანე რიცხვი 1- დან 10-მდე"))

if ricxvi > 10:
    print("დადებითია")

elif ricxvi < 10:
    print("არასწორია")
else:
    print("უარყოფითია")

for i in range(2, 21, 2):
    print(i)

for i in range(1,22, 2 ):
    print(i)

qula = int(input("შენი გამოცდის ქულა"))

if qula >51:
    print("მალადეც")

elif qula <50:
    print("ვერ ჩააბარე")