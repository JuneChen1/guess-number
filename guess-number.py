import random

pwdList = random.sample(range(0, 10), 4)
A = 0
B = 0

while A != 4:
  num = input("請輸入四個數字：")
  while num.isdigit() == False or len(num) != 4 or len(set(num)) != 4:
    num = input("請輸入四個數字，且數字勿重複：")
  
  numList = list(map(int, list(num)))
  A = 0
  B = 0
  for i in numList:
    if i in pwdList:
      if numList.index(i) == pwdList.index(i):
        A += 1
      else:
        B += 1
  
  print("{}：{}A{}B".format(num, A, B))
  
print("恭喜猜對！密碼是：" + num)  