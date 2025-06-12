month = int(input("შეიყვანე შენი დაბადების დღის თვე"))

if month >= 1 and month <= 3:
    print("ზამთარი")

elif month >= 4 and month <= 6:
    print("გაზაფხული")

elif month >= 7 and month <= 9:
    print("ზაფხული")

elif month >= 10 and month <= 12:
    print("შემოდგომა")



ricxvi = int(input("შეიყვანე რიცხვი 0-დან 10-მდე"))

if ricxvi > 0:
    print("დადებითია")

elif ricxvi < 0 :
    print("უარყოფითია")

else:
    print("რიცხვი ნულია")



#if არის: თუ (რაღაცა)
#else არის: სხვა შემთხვევაში
#elif არის იგივე if უბრალოდ ვიყენებთ რამდენჯერაც გვინდა ანუ, if-ს რომ დავწერთ და კიდევ გვინდა if-ის დაწერა, მაგის მაგივრად დავწერთ elif-ს უსასრულოდ

age = int(input("შეიყვანე შენი ასაკი"))
income = int(input("შეიყვანე შენი შემოსავალი"))

if age < 18 and income <10000:
    print("განთავისუფლებული ხარ")


else:
    print("გადასახადი გადასახდელია")


ricxvi = int(input("შეიყვანე რიცხვი 1 დან 10 მდე"))

if ricxvi > 10:
    print("მეტია")

else:
    print("ნაკლებია")