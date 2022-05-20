import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
tn=int(len(names))
random_num=int(random.randint(0,tn-1))
random_name=random.choice(names[random_num])
print(random_name,'is goint to pay the bill')