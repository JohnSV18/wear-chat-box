from random import choice
def get_box_response(user_response):

    bot_response_hot = ["wear shorts", "Wear something light","wear a t-shirt"]
    bot_response_cold = ["wear a coat", "wear a scarf", "wear a hat"]
    bot_response_chilly = ["wear a hoodie", "wear a beanie", "wear a thick flanel"]

     if user_response == "hot":
        return choice(bot_response_hot)
    elif user_response == "cold":
        return choice(bot_response_cold)
    elif user_response == "chilly":
        return choice(bot_response_chilly)
    else:
        return "I'm not sure what you should wear"

