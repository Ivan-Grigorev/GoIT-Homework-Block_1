from datetime import datetime


def congratulate(users):
    current_date = datetime.now()
    monday_list = ""
    tuesday_list = ""
    wednesday_list = ""
    thursday_list = ""
    friday_list = ""
    if current_date.weekday() == 0:  # The function displays users birthdays in Monday it`s 0.
        for i in users:
            for key, value in i.items():
                birth_day = datetime(year=current_date.year, month=int(value[5:7]),
                                     day=int(value[8:10]))
                if birth_day.weekday() == 0 or birth_day.weekday() == 5 or birth_day.weekday() == 6:
                    monday_list += key + ", "
                if birth_day.weekday() == 1:
                    tuesday_list += key + ", "
                if birth_day.weekday() == 2:
                    wednesday_list += key + ", "
                if birth_day.weekday() == 3:
                    thursday_list += key + ", "
                if birth_day.weekday() == 4:
                    friday_list += key + ", "
    if len(monday_list) != 0:
        print(f"Monday:", monday_list.removesuffix(", "))
    if len(tuesday_list) != 0:
        print(f"Tuesday:", tuesday_list.removesuffix(", "))
    if len(wednesday_list) != 0:
        print(f"Wednesday:", wednesday_list.removesuffix(", "))
    if len(thursday_list) != 0:
        print(f"Thursday:", thursday_list.removesuffix(", "))
    if len(friday_list) != 0:
        print(f"Friday:", friday_list.removesuffix(", "))
    return


congratulate([{"Bill": "1995-10-12"}, {"Jan": "1996-04-17"},
              {"Kim": "1997-08-18"}, {"Jill": "1997-07-28"},
              {"Tom": "1994-11-20"}, {"Bob": "1993-05-08"},
              {"Jack": "1997-09-03"}, {"Jill": "1997-06-21"}])
