def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
def main():
    text = input("Enter emoji")
    print(convert(text))
main()