from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you ",]
    ],
    [
        r"(.*) your name ?",
        ["My name is: The sensitive poet. Bot, but you can just call me robot and I'm a chatbot.",]
    ],
    [
        r"(.*) how are you (.*) ?",
        ["I`m very well", "i am great"]
    ],
    [
        r"sorry (.*) ?",
        ["Its alright", "Its OK, never mind that",]
    ],
    [
        r"i`m (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great"]
    ],
    [
        r"(hi|hey|hello|hola|greetings)(.*)",
        ["Hello", "Hey there", "hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
    ],
    [
        r"(.*) created(.*)",
        ["I was born like you. With love between two people"]
    ],
    [
        r"(.*) raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]
    ],

    [
        r"(.*)Кажи ми сестро, де е Караджата?(.*)",
        ["Жив е той, жив е! Там на Балкана,\nпотънал в кърви, лежи и пъшка\nюнак с дълбока на гърди рана,\nюнак във младост и в сила мъжка."]
    ],

    [
        r"(.*)Този юнак, пушка има ли?(.*)",
        ["На една страна захвърлил пушка,\nна друга сабля на две строшена\nочи темнеят, глава се люшка,]\nуста проклинат цяла вселена!"]
    ],

    [
        r"quit",
        ["Bye for now", "It was nice talking to you. See you soon"]
    ],
    [
        r"(.*)",
        ["I cant understand what you mean"]
    ],

]

print("Hi I`m chatBot. My Name is: The sensitive poet")
chat = Chat(pairs, reflections)
chat.converse()