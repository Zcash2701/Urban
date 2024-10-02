numb_list = [42, 69, 322, 13, 10, -99, 5, 9, 8, 7, -6, 5]
count = 0
while count < len(numb_list):
    if numb_list[count] <= 0:
        break
    else:
        print(numb_list[count])
    count += 1
