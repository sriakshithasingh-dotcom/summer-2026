def main():
    time = input("What is the time:")
    converted = convert(time)
    if 7.0 <= converted <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted <= 13.0:
        print("lunch time")
    elif 18.0 <= converted <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
