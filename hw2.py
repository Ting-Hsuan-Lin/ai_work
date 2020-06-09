import random
print("想不到下一餐要吃甚麼嗎？讓pyhon幫你決定！")
print("最多可輸入99種餐點，輸入完畢請輸入Done")
food_choice=[]
count=99
for i in range(count):
    food=input("請輸入想吃的食物:")
    
    if (food)!="Done":
        if i !=3:
            food_choice.append(food)
        else:
            print("您已達數量上限")
            break
    else:
        print("以下是你想吃的食物:")
        print (food_choice)
        break


print ("以下是系統幫你選的食物:")
print (random.choice(food_choice))

