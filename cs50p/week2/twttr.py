text = input("Input: ")
output = ""
for char in text:
    if char not in ["A","E","I","O","U","a","e","i","o","u"]:
        output =  output + char
    print("Output:",output)

