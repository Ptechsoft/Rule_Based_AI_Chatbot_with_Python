# Importing Packages 
import time
import random
import sys

AI = "DecoBot" #Name of the AI bot

Lab = "Decodelabs"

# Loading text
def boot_sequence():
    messages = [
    "intializing DecoBot",
    "Loading Knowledge Base",
    "System Online",
    "Welcome to DecoBot AI Terminal \n"
    ]

    #Time for the loading text
    for msg in messages:
        print(msg)
        time.sleep(0.8)  # Pause between each line

def type_effect(text, speed=0.03):
    # Prints text character by character like someone typing
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
    # Punctuation gets a longer pause — feels natural
        if char == ".":
            time.sleep(0.15)
        else:
            if char == ",":
                time.sleep(0.08)
            else:
                if char == "!":
                    time.sleep(0.12)
                else:
                    time.sleep(speed)
    print()

def thinking_effect():
    # Simulates DecoBot "thinking" before responding
    thoughts = [
        "Thinking",
        "Processing",
        "Analyzing",
        "Computing",
    ]
    word = random.choice(thoughts)
    sys.stdout.write(f"{AI}: {word}")
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(0.4)
        sys.stdout.write(".")
        sys.stdout.flush()
    # Clear the thinking line
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

# Sanitizing the user input
def sanitize_input(raw):
    clean = raw.strip().lower() # Convertion to lower case
    clean = clean.replace("?", "").replace("!", "").replace(".", "")
    return clean

# Mood detection
def detect_mood(clean):
    happy_words    = ["happy", "great", "awesome", "excited", "love", "good", "amazing"]
    angry_words    = ["angry", "frustrated", "hate", "stupid", "useless", "annoyed"]
    confused_words = ["confused", "lost", "dont understand", "what do you mean", "huh"]
    sad_words      = ["sad", "tired", "bored", "stuck", "difficult", "hard", "struggling", "depressed"]

    if any(word in clean for word in happy_words):
        return "happy"
    else:
        if any (word in clean for word in angry_words):
            return "angry"
        else:
            if any (word in clean for word in confused_words):
                return "confused"
            else:
                if any(word in clean for word in sad_words):
                    return "sad"
                else:
                    return "neutral"

#Greetings 
def classify_input(clean):
    greetings     = ["hi", "hey", "hello", "howdy", "yo"]
    acknowledgements = ["ok", "okay", "k", "alright", "got it", "sure"]
    
    if clean == "":
        return "empty"
    else:
        if clean in greetings: # Check greetings first before anything else
            return "greetings"
        else:
            if clean in acknowledgements: # Check acknowledgemenet first before anything else
                return "acknowledgement"
            else: # Checking for words
                if clean.startswith(("what", "how", "why", "when", "who")):
                    return "question"
                else:
                    return "statement"

def extract_name(clean):
    # Handles: "my name is john", "i am john", "call me john"
    if "my name is" in clean:
        return clean.split("my name is")[-1].strip().title()
    else:
        if "i am" in clean:
            # make sure it's a name not a mood e.g "i am happy"
            mood_words = ["happy", "sad", "angry", "confused", "tired", "okay", "good"]
            potential  = clean.split("i am")[-1].strip().title()
            if potential.lower() not in mood_words:
                return potential
            else:
                return None
        else:
            if "call me" in clean:
                return clean.split("call me")[-1].strip().title()
            else:
                return None

# 
def get_response(clean, mood, memory):
    knowledge_base = {
        # Question and responses store in a dictionary usinf key and values
        "what is ai"              : "AI is the simulation of human intelligence by machines using logic and data.",
        "what is machine learning": "Machine learning is AI that learns from data instead of explicit rules.",
        "what is a chatbot"       : "A chatbot is a program that simulates conversation — like me!",
        "what is deep learning"   : "Deep learning uses neural networks with many layers to learn complex patterns.",
        "what is python"          : "Python is the most popular language for AI and data science.",
        "what is a dictionary"    : "A dictionary stores key-value pairs — exactly how my knowledge base works!",
        "what is a loop"          : "A loop repeats a block of code — my while True loop keeps me alive!",

        "what is decodelabs"      : "DecodeLabs is your internship home where you become a real AI engineer!",
        "what is project 1"       : "Project 1 is me a rule-based AI chatbot built on control flow and logic.",
        "what is the ipo model"   : "IPO stands for Input, Process, Output — the blueprint of every AI system.",
        "how do i pass project 1" : "Build the loop, sanitize input, create a knowledge base, add fallback, and exit cleanly.",
        "why is python used in ai": "Python is simple, power ful, and has libraries like TensorFlow and PyTorch for AI.",
        "who made you"            : "I was built by Nwadigo Praise a DecodeLabs intern possibly a future AI engineer!",
    }

    # Dictionary containing the mood and the response using
    mood_prefix = {
            "happy"  : "Love the energy! ",
            "angry"  : "I hear you, let's work through this. ",
            "confused": "No worries, let me break it down. ",
            "sad"    : "Hang in there! ",
            "neutral" : ""
        }
    
    # Personalize with name if we know it
    name        = memory["name"]
    msg_count   = memory["message_count"]
    name_prefix = f"{name}, " if name else ""

    prefix = mood_prefix[mood]

    #Milestone messages based on message count
    if msg_count == 5:
        milestone = "⚡ 5 messages in you're on a roll!\n"
    else:
        if msg_count == 10:
            milestone = "🔥 10 messages! You're really digging into this.\n"
        else:
            if msg_count == 20:
                milestone = "🚀 20 messages! You might just be a real AI engineer.\n"
            else:
                milestone = ""

#--------- KNOWLEDGE LOOKUP
    if clean in knowledge_base:
        return milestone + prefix + name_prefix + knowledge_base[clean]
    else:
        if "ai" in clean:
            return milestone + prefix + name_prefix+ "AI is a based field, can you be more specific?"
        else:
            if "project" in clean:
                return milestone + prefix + name_prefix+ "This project is about rule based logic. Master the fundamentals first!"
            else:
                if  "help" in clean:
                    return milestone + prefix + name_prefix+ "Try asking: 'what is ai', 'what is python', or 'how do i pass project 1'."
                else:
                    fallback = [
                        "Hmm, I don't have that in my knowledge base yet.",
                        "Interesting, but I'm not trained on that yet.",
                        "I'm still learning! Try asking something about AI or DecodeLabs.",
                    ]
                    return milestone + prefix + name_prefix + random.choice(fallback)
def chatbot():
    boot_sequence()
    print()

    openers = [
        "Every great AI engineer started exactly where you are.",
        "Rule based logic is the skeleton of all intelligence.",
        "The best time to build was yesterday. Second best is now.",
    ]
    type_effect(f"💡 {random.choice(openers)}\n", speed=0.03)
    time.sleep(0.5)

    sys.stdout.write("DecoBot: Before we begin, what's your name? ")
    sys.stdout.flush()


    raw_name     = input()
    clean_name = raw_name.strip().lower()
    entered_name = raw_name.strip().title()

    # Reuse extract_name() to handle all cases
    extracted  = extract_name(clean_name)
    
    if extracted:
        entered_name = extracted
    else:
    # They typed just their name directly e.g "Praise"
        entered_name = raw_name.strip().title()

    if entered_name == "":
        entered_name = "Intern"


    # MEMORY BANK:
    memory = {
        "name"         : entered_name,    # user's name once told
        "greeted"      : False,   # so we never say Welcome twice
        "message_count": 0        # tracks conversation length
    }

    type_effect(f"\nDecoBot: Great to meet you, {memory['name']}! I'm DecoBot, your DecodeLabs AI assistant.")
    type_effect(f"DecoBot: Ask me anything about AI or Python.\n")
    time.sleep(0.5)


    while True:
        raw_input = input("You:")

        if raw_input.strip().lower() in ("quit", "exit"):
            print(f"\n{AI}: Shutting down... Stay curious. Goodbye!")
            time.sleep(1)
            break
        
        # INCREMENT MESSAGE COUNT
        memory["message_count"] += 1

        clean = sanitize_input(raw_input)

        # CHECK IF USER IS TELLING US THEIR NAME
        detected_name = extract_name(clean)
        if detected_name:
            memory["name"] = detected_name
            print(f"{AI}: Got it! I'll call you {memory['name']} from now on.\n")
            continue

        # CLASSIFY 
        input_type = classify_input(clean)

        # DETECT MOOD
        mood = detect_mood(clean)

        #Thinking effect of the bot
        thinking_effect()

        # RESPOND
        if input_type == "empty":
            print(f"{AI}: You didn't type anything. Try again. \n")
        else: 
            # first time greeting vs returning greeting
            if input_type == "greetings":
                if not memory["greeted"]:
                    memory["greeted"] = True
                    if mood == "happy":
                        print(f"{AI}: Hey hey, {memory['name']} Great vibes! Welcome to DecodeLabs!\n")
                    else:
                        print(f"{AI}: Hey 😊 {memory['name']} Ready to learn some AI? Ask me anything!\n")
                else:
                    # Already greeted — respond naturally, not robotically
                    responses = [
                            f"Still here, {memory['name']}! What else can I help with?",
                            f"Hey again, {memory['name']}! Got more questions?",
                            f"You rang, {memory['name']}? 😄",
                        ]
                    print(f"{AI}: {random.choice(responses)}\n")

            else:
                if input_type == "acknowledgement":
                    print(f"{AI}: Got it, {memory['name']}! Let me know if you need anything else.\n")
                else:
                    response = get_response(clean, mood, memory)
                    print(f"{AI}: {response}\n")
chatbot()