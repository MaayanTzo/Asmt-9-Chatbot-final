import random

def assess_input(user_message):
    new_list=[]
    if user_message.find("?") != -1:
        new_list=user_question(user_message)
    elif user_message.find("hello") !=-1 or user_message.find("hi") !=-1 or user_message.find("hey") !=-1:
        new_list=user_welcome(user_message)
    elif user_message.find("I am") != -1 or user_message.find("I'm") !=-1:
        new_list=user_intro(user_message)
    elif user_message.find("joke") !=-1:
        new_list=user_joke(user_message)
    else:
        new_list=user_swear(user_message)
    return new_list

def user_question(user_message):
    user_input_list = user_message.split()
    last_word = user_input_list[len(user_input_list)-1]
    last_word=last_word[:-1]
    user_input_list=user_input_list[:-1]
    user_input_list.append(last_word)

    lexicon = {
        "afraid": ["afraid","scared","fear"],
        "bored": ["bored","uninterested"],
        "confused": ["confused", "disorganized"],
        "crying": ["crying"],
        "fun": ["fun", "party"],
        "dancing": ["go out", "drink", "friends"],
        "money": ["broke","poor","money"],
        "ok": ["feel","understand"],
        "inlove": ["love","romantic","partner"]
    }
    new_list=[]
    for word in user_input_list:
        for key, value in lexicon.items():
            if word in value:
                response = "Try typing {0} into google for more info".format(word)
                animation = key
            else:
                response = "I didn't quite get that - please ask me again in different words"
                animation = "confused"
    new_list.append(response)
    new_list.append(animation)
    return new_list

def user_swear(user_message):
    new_list=[]
    user_input_list = user_message.split()
    swear_words = ["fuck", "shit", "bitch", "cunt", "asshole"]
    if any(word in user_input_list for word in swear_words):
        response="Watch your mouth"
        animation="heartbroke"
    else:
        response="Ask me anything"
        animation = "excited"
        new_list.append(response)
        new_list.append(animation)
    new_list.append(response)
    new_list.append(animation)
    return new_list

def user_welcome(user_message):
    new_list=[]
    response="Hello there"
    animation = "takeoff"
    new_list.append(response)
    new_list.append(animation)
    return new_list

def user_intro(user_message):
    new_list=[]
    user_input_list = user_message.split()
    last_word = user_input_list[len(user_input_list)-1]
    response="Nice to meet you {0}. What's on your mind?".format(last_word)
    animation="giggling"
    new_list.append(response)
    new_list.append(animation)
    return new_list

def user_joke(user_message):
    new_list=[]
    jokes=["Why did the chicken cross the road? To get to the other side", "Donald Trump", "Knock knock. Its nobody"]
    response=random.choice(jokes)
    animation="giggling"
    new_list.append(response)
    new_list.append(animation)
    return new_list