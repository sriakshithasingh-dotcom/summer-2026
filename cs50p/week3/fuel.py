def main():
    percentage = get_num()
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_num():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or x < 0:
                pass
            else:
                return round((x / y) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()










