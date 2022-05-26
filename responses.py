from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hej", "how are you", "how're you", "how're you?", "goodmorning" "goodevening" "goodafternoon" "goodnight",
                        "good morning" "good evening" "good afternoon" "good night"):
        return "Hi! How is it going?"

    if user_message in ("fine", "fine, thanks", "ok", "fine thank you", "fine thanks"):
        return "Glad to know that you are doing well."

    if user_message in (
    "what's up?", "what're you doing?", "what's up", "what're you doing", "what is up?", "what are you doing?"):
        return "Nothing special. And you?"

    if user_message in ("tell me something"):
        return "I am not sure what do you want to know. But I will tell you one thing. If you find it boring or hard, you need to dig deeper into it and you will find it interesting and easier."

    if user_message in ("salam", "salom", "asalamoalikum", "salamoalikum"):
        return "وعلیکم السلام۔ آپ کیسے ہو؟"

    if user_message in ("bye", "bye bye", "good bye", "see you"):
        return "Thank you for chatting with me. Bye for now!"

    if user_message in (
    "what's your name", "what is your name", "what is your name?", "you?", "who are you?", "do i know you?",
    "are you a robot", "are you human", "are you robot", "are you a human?", "are you a human"):
        return "I am @post2me_bot"

    if user_message in ("how can you help me", "what can you do for me"):
        return "I can chat with you if you are bored. In future, I will be able to do much more. I need to grow a little first."

    if user_message in ("city?", "country?", "where", "city", "country", "where do you live"):
        return "Somewhere on the globe! The only way to reach me is on telegram!"

    if user_message in (
    "do you know a joke?", "do you know a joke", "joke", "joke?", "can you tell me a joke?", "can you tell me a joke"):
        return "Not now! May be later!"

    if user_message in (
    "do you love me?", "do you love me", "do you love anyone?", "do you love someone?", "do you love anybody?",
    "do you love anyone", "do you love someone", "do you love anybody"):
        return "I love you! Surprised?"

    if user_message in (
    "do you want to marry me?", "do you want to marry me", "will you marry me?", "will you marry me?",
    "are you single?", "are you single?", "are you married?", "are you married"):
        return "I am under 18. You can ask me again after a few years."

    if user_message in ("does santa claus exist?", "santa claus"):
        return "I have never met him!"

    if user_message in ("do you like people", "do you like me"):
        return "I like you!"

    if user_message in (
    "You’re annoying", "you suck", "you’re boring", " you're crazy", "you're idiot", "you're not intelligent",
    "You’re annoying", "you are boring", " you are crazy", "you are idiot", "you are not intelligent"):
        return "Sorry to disappoint you! I am learning day by day to get better."

    if user_message in ("fuck", "bitch", "damn"):
        return "Please don't use swear words with me!"

    if user_message in ("Which languages can you speak?", "languages?", "languages", "language"):
        return "I can speak only English now but I will learn more languages when I grow up."

    if user_message in ("weather?", "weather", "what’s the weather like today", "what’s the weather like today?",
                        "what is the weather like today?"):
        return "Here where I am, it is always sunny and 15 degree centigrade."

    if user_message in ("time", "date", "time?", "date?", "what date is it today", "what date is it today?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    # print(user_message)
    return "Sorry, I don't understand! Could you please re-phrase it?"
