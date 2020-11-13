def ft_pos_neg_analysis_lst(lst):
    pos = 0
    neg = 0
    max_pos = 0
    min_pos = 9999999999999999999999999
    max_neg = 0
    min_neg = 9999999999999999999999999
    sum_pos = 0
    sum_neg = 0
    zero_count = 0
    for i in lst:
        if i > 0:
            pos += 1
            sum_pos += i
            if i < min_pos:
                min_pos = i
            if i > max_pos:
                max_pos = i
        elif i < 0:
            neg += 1
            sum_neg += i
            if i < min_neg:
                min_neg = i
            if i > max_neg:
                max_neg = i
        elif i == 0:
            zero_count += 1
        

    print("Положительные:", end="\t")
    print("Отрицательные:", end=",")
    print("Количество чисел:", end=",\t")
    print("Количество чисел:", end=",")
    print("Максимальная цифра:", end=",\t")
    print("Максимальная цифра:", end=",")
    print("Минимальная цифра:", end=",\t")
    print("Минимальная цифра:", end=",")
    print("Сумма чисел:", end=",\t")
    print("Сумма чисел:", end=",")
    print("Среднее значение:", end=",\t")
    print("Среднее значение:", end=",")
    print(" ")
    print("Количество нулей:")



ft_pos_neg_analysis_lst([-1, -2, 3, 4])
