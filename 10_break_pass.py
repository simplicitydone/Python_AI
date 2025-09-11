cup = 0
                        # 또는 running = True, while running:
# while True:
#     cup += 1
#     print(cup)
#     if cup == 10:
#         break           # 또는 running = False

# print('while 문 종료')

for i in range(1,10):
    if i == 3:
        continue
    elif i ==6:
        continue
    elif i ==9:
        continue
    print(i)

print()

for i in range(1,10):
    if i == 3 or i == 6 or (i == 9):
        continue
    print(i)

print()

for i in range(1,10):
    if i in (3,6,9):
        continue
    print(i)

print()

for i in range(1,10):
    if i % 3 ==0:
        continue
    print(i)
