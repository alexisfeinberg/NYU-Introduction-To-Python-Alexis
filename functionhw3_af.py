def sleep_in ():
    return input("What is the day of the week?\n")

def week_logic (day_week):
    if day_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
        print("Do not sleep in! Get yourself to work!")
    elif day_week == "Saturday" or day_week == "Sunday":
        print("Sleep in!")
    else:
        print("Try typing the day of the week again")

def main():
    day_of_week=sleep_in()
    week_logic(day_week=day_of_week)


if __name__ == '__main__':
    main()
