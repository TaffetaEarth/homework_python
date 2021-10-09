def check(day, month, year):
    """Hello! This is our DateCheck function. Hope it works correctly."""
    d = {"January": [31, 1], "February": [28, 2], "March": [31, 3], "April": [30, 4], "May": [31, 5], "June": [30, 6],
         "July": [31, 7], "August": [31, 8], "September": [30, 9], "October": [31, 10], "November": [30, 11],
         "December": [31, 12]}
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November", "December"]
    now_day = 9
    now_month = "October"
    now_year = 2021
    if year % 4 == 0:
        d["February"][0] = 29
    if month in month_list:
        if year == now_year:
            if d.get(month)[1] == d.get(now_month)[1]:
                if day <= now_day and (day > 0):
                    return True
                else:
                    return False
            elif month < now_month:
                return True
            else:
                return False
        elif year < now_year:
            if d.get(month)[1] < 12:
                if day <= d.get(month)[0] and (day > 0):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return "Неправильное название месяца!"


print(check(29, "February", 2019))
help(check)
