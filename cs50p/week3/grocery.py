def main():
    counts = {}

    while True:
        try:
            item = input().lower()
            if item in counts:
                counts[item]+=1
            else:
                counts[item] = 1
        except EOFError:
            break
    for item in sorted(counts):
        print(counts[item],item.upper())
main()






