def chatbot():
    print("-----A Simple Chatbot-----")
    
    while True:
        user = input("you:".lower())
        
        if user == "hello":
            print("Chatbot: Hi!")
            
        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")
            
        else:
            print("Chatbot: Sorry, I don't understand.")
            
chatbot()