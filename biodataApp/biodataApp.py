# Made with ♥ by Saepul Bahri (TI22I International - 20220040277)

def getUserBio():
    # get user name
    name = input("Your name: ")
    # get user age
    age = int(input("your age: "))
    # get user major
    major = input("Your major: ")
    # do user like spicy food
    isLikeSpicy = bool(
        input("Do you like spicy food? (enter y = yes or press 'Enter' to skip) "))
    # user hobbies
    hobbies = []
    while 1 < 2:
        getHobbies = input(
            "Enter your hobbies! (enter '/' to escape or quit the form) ")
        if getHobbies == '/':
            break
        hobbies.append(getHobbies)
    # user motto
    quote = input("A phrase or sentence that you can live by: ")

    # it's just a fancy separator
    print("=====================")

    # print name, age, and major to the screen
    print("Your name is", name.capitalize())
    print("Your are", str(age), "years old")
    print("You study", major.capitalize())
    if isLikeSpicy:
        print("You like spicy food")
    else:
        print("You don't like spicy food")
    if len(hobbies):
        print("You like to spend your spare time by", ", ".join(hobbies))
    else:
        print("You don't have a hobby :(")
    print("Your life motto: ", quote)

    # it's just a fancy separator
    print("=====================")

    print("name data type:", type(name))
    print("age data type:", type(age))
    print("major data type:", type(major))
    print("hobbies data type:", type(hobbies))
    print("isLikeSpicy data type:", type(isLikeSpicy))
    print("quote data type:", type(quote))


getUserBio()
