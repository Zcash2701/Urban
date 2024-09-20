numb_list = [42, 69, 322, -13, 0, 99, 5, 9, 8, 7, -6, 5]
flag = True
count = 0
while flag:
    if count == len(numb_list) or numb_list[count] < 0:
        flag = False
        continue
    else:
        print(numb_list[count])
    count += 1