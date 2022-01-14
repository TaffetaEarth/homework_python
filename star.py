def password(password):
    result = []
    sub_result = []
    values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for f in password:
        for i in range(len(values)):
            if int(f) in values[i]:
                if i != 0 and i != len(values) - 1:
                    num = values[i].index(int(f))
                    if not result:
                        if num == 0 or num == len(values[i]) - 1:
                            result.append(f)
                            result.append(str(values[i][abs(num - 1)]))
                            result.append(str(values[i - 1][num]))
                            result.append(str(values[i + 1][num]))
                            print(1)
                        else:
                            result.append(f)
                            result.append(str(values[i + 1][num]))
                            result.append(str(values[i - 1][num]))
                            result.append(str(values[i][num + 1]))
                            result.append(str(values[i][num - 1]))
                            print(2)
                        print(sub_result)
                    else:
                        if num == 0 or num == len(values[i]) - 1:
                            for k in result:
                                sub_result.append(str(k) + f)
                                sub_result.append(str(k) + str(values[i][abs(num - 1)]))
                                sub_result.append(str(k) + str(values[i - 1][num]))
                                sub_result.append(str(k) + str(values[i + 1][num]))
                                print(f)
                        else:
                            print(4)
                            print(result)
                            for k in result:
                                sub_result.append(str(k) + f)
                                sub_result.append(str(k) + str(values[i - 1][num]))
                                sub_result.append(str(k) + str(values[i + 1][num]))
                                sub_result.append(str(k) + str(values[i][num + 1]))
                                sub_result.append(str(k) + str(values[i][num - 1]))
                        if sub_result:
                            result = sub_result
                        print(sub_result)
                        sub_result.clear()
                else:
                    num = values[i].index(int(f))
                    if not result:
                        if num == 0 or num == len(values[i]) - 1:
                            print(5)
                            result.append(f)
                            result.append(str(values[i][abs(num - 1)]))
                            result.append(str(values[abs(i - 1)][num]))
                            print(result)
                        else:
                            print(6)
                            result.append(f)
                            result.append(str(values[abs(i - 1)][num]))
                            result.append(str(values[i][num + 1]))
                            result.append(str(values[i][num - 1]))
                            print(result)
                    else:
                        if num == 0 or num == len(values[i]) - 1:
                            print(7)
                            for k in result:
                                sub_result.append(str(k) + f)
                                sub_result.append(str(k) + str(values[i][abs(num - 1)]))
                                sub_result.append(str(values[abs(i - 1)][num]))
                        else:
                            print(8)
                            for k in result:
                                sub_result.append(str(k) + f)
                                sub_result.append(str(k) + str(values[abs(i - 1)][num]))
                                sub_result.append(str(k) + str(values[i][num + 1]))
                                sub_result.append(str(k) + str(values[i][num - 1]))
                        if sub_result:
                            result = sub_result
                        print(result)
                        sub_result.clear()
    return result


print(password("1635"))
