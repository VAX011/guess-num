import random
start = input('請輸入隨機數字開始值')
end = input('請輸入隨機數字結束值')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print('你猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
    	print('再小一點')
    elif num < r:
    	print('再大一點')
    print('這是你猜的第', count ,'次')