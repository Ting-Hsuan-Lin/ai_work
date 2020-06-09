import random

final_number=random.randint(1,100)
min=0
max=100
i=1
print('定時炸彈即將爆炸，需要猜對終極密碼才能使炸彈停止，您有3次機會')
print('密碼為1~100的整數')
for i in range(1,4):
    test=int(input("請輸入密碼: "))
    if test != final_number: 
        if test>final_number:
            if i !=3:
                max=test
                print("提示：",min,"~",max)           
                i=i+1
            else:
                print("您已失敗！爆炸了！！")
        else:
            if i!=3:  
                min=test
                print("提示：",min,"~",max)
                i=i+1
            else:
                print("您已失敗！爆炸了！！")
            


    else:
       print("恭喜你，炸彈已解除")
       break

