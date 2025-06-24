#ინდექსინგი გვაძლევს საშუალებას, კონკრეტულ ელემენტზე მივწვდეთ

#2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[4] = 5
print(nums[2:])

#3
#Slicing (დაჭრა) არის მონაცემთა ნაწილის ამოღება – მაგალითად, სტრიქონიდან ან სიიდან
text = "hello world earth"
nums = [1,2,3,4,5,6,7,8,9,10]
print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::2])
print(text[::-1])

#4
my_list = list(range(1, 81))
my_list[64] = "gurami"
print(my_list[-16])
