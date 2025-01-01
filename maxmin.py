def maxmin(int_list):

    current_max = int_list[0]
    current_min = int_list[0]

    for i in range(len(int_list)):
        if int_list[i] < current_min:
            current_min = int_list[i]
        elif int_list[i] > current_max:
            current_max = int_list[i]

    return [current_min, current_max]


print(maxmin([100, -100]))
