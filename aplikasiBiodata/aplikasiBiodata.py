# Biodata app made by Saepul Bahri

def get_user_bio():
    # get user name
    name = input("Your name: ")
    # get user age
    age = input("your age: ")
    # get user major
    major = input("Your major: ")

    # it's just a fancy separator
    print("=====================")

    # print user name, age, and major to the screen
    print("Nama anda adalah:", name)
    print("Umur anda:", age)
    print("Anda berada di jursan:", major)


get_user_bio()
