import subprocess
import time

author = "Jencent Dizon"
link = "https://github.com/I-am-Programmer-101"
print("Author:", author, "\t\tLink:",link)

def Replace_Text():
    print("example : C:/Users/Admin/Documents/test.txt")

    filename = input("Enter a filename.txt: ")

    with open(filename, "r") as file:
        test = file.read()
        print("\nORIGINAL TEXT: " + test + "\n")

    old_txt = input("[*] Old Text: ")

    file = open(filename, "w+")
    for i in range(1):
        new_txt = input("[*] New Text: ")
        file.write(test.replace(old_txt, new_txt))
    file.close()

    with open(filename, "r") as file:
        new_text = file.read()
        print("\nNEW TEXT: " + new_text)
        print("\n[+] Replace Text Success")

    input("Press Enter to exit.")

if __name__ == "__main__":
    Replace_Text()
