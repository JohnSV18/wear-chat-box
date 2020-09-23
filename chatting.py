from random import choice
#function is created with the parameter "user_response"
def get_box_response(user_response):

#the lists of strings are created that are also the bot responses depending on what They’ve say
    bot_response_hot = ["wear shorts", "Wear something light","wear a t-shirt"]
    bot_response_cold = ["wear a coat", "wear a scarf", "wear a hat"]
    bot_response_chilly = ["wear a hoodie", "wear a beanie", "wear a thick flanel"]

#an if statement checks the user input and depending on what it says then returns an item from a list
     if user_response == "hot":
        return choice(bot_response_hot)
    elif user_response == "cold":
        return choice(bot_response_cold)
    elif user_response == "chilly":
        return choice(bot_response_chilly)
    else:
        #if none of the words specified are inserted then you state that you
        #don't know how to help them
        return "I'm not sure what you should wear"
##this prints out what the chat box does
print("Welcome to the clothing chat box, where we tell \n" + 
        "you what to wear based on the weather (Kind of)")
# a while loop that is always true so that the user can input how it feels outside
# and the program will continue asking until the user inputs "done"
 while True:
    user_response = input("How does it feel outside? (hot, cold, chilly) ?")

    if user_response == 'done':
        break

#a new variable is created that stores the value of the function with the 1 parameter
    bot_response = get_ebot_response(user_response)
#what is stored in the new variable is then printed
    print(bot_response)


