print("welcome to equity bank")
name=input("enter your name")
print("welcome",name,"to the bank")
print("please enter the amount you would like to withdraw")
amount=int(input("enter the amount:"))
note1000=amount//1000
note500=(amount%1000)//500
note200=((amount%1000)%500)//200
note100=(((amount%1000)%500)%200)//100
note50=((((amount%1000)%500)%200)%100)//50
print("1000 notes=",note1000)
print("500 notes=",note500)
print("200 notes=",note200)
print("100 notes=",note100)
print("50 notes=",note50)
