def validator(field):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    counter = 0
    for x in range(10):
        for j in range(10):
            if field[x][j] == 1:
                counter += 1
            else:
                if counter == 1:
                    ones += 1
                elif counter == 2:
                    twos += 1
                elif counter == 3:
                    threes += 1
                elif counter == 4:
                    fours += 1
        counter = 0


    def check_level(start_x, start_j):
        while field[start_x + 1] != 0 or field[start_x - 1]


    # counter = 0
    # for x in range(9):
    #     for j in range(9):
    #         if field[j][x] == 1:
    #             counter += 1
    #         else:
    #             if counter == 1:
    #                 ones += 1
    #             elif counter == 2:
    #                 twos += 1
    #             elif counter == 3:
    #                 threes += 1
    #             elif counter == 4:
    #                 fours += 1
    #     counter = 0





    # def check_around(start_x, start_j, level, position):
    #     flag = True
    #     if position == "horizontal":
    #         if level == 1:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 2):
    #                     if field[i][k] == 1 and i != start_x and k != start_j:
    #                         flag = False
    #         if level == 2:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 3):
    #                     if field[i][k] == 1 and i != start_x and k != start_j \
    #                             and k != start_j+1:
    #                         flag = False
    #         if level == 3:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 4):
    #                     if field[i][k] == 1 and i != start_x and k != start_j \
    #                             and k != start_j+1 and k != start_j+2:
    #                         flag = False
    #         if level == 4:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 5):
    #                     if field[i][k] == 1 and i != start_x and k != start_j \
    #                             and k != start_j+1 and k != start_j+2 and k != start_j+3:
    #                         flag = False
    #     if position == "vertical":
    #         if level == 1:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 2):
    #                     if field[i][k] == 1 and i != start_x and k != start_j:
    #                         flag = False
    #         if level == 2:
    #             for i in range(start_x - 1, start_x + 3):
    #                 for k in range(start_j - 1, start_j + 2):
    #                     if field[i][k] == 1 and k != start_x and i != start_j \
    #                             and i != start_j + 1:
    #                         flag = False
    #         if level == 3:
    #             for i in range(start_x - 1, start_x + 4):
    #                 for k in range(start_j - 1, start_j + 2):
    #                     if field[i][k] == 1 and k != start_x and i != start_j \
    #                             and i != start_j + 1 and i != start_j + 2:
    #                         flag = False
    #         if level == 4:
    #             for i in range(start_x - 1, start_x + 2):
    #                 for k in range(start_j - 1, start_j + 5):
    #                     if field[i][k] == 1 and k != start_x and i != start_j \
    #                             and i != start_j + 1 and i != start_j + 2 and i != start_j + 3:
    #                         flag = False
    #     return flag

