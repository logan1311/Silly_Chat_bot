import json
import random
import datetime
from datetime import date
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class SimpleChatBot:
    def __init__(self, name="LocalBuddy"):
        self.name = name
        self.conversation_history = []
        
    def get_response(self, user_message):
        user_lower = user_message.lower()
        
        # Greetings
        if any(word in user_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            responses = [
                "Hello! I'm your local chatbot! 😊",
                "Hi there! Nice to meet you! 🤖",
                "Hey! I'm here to chat with you! 🌟"
            ]
            return random.choice(responses)
        
        # Time
        elif any(word in user_lower for word in ['time', 'current time']):
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            return f"⏰ The current time is {current_time}"
        
        # Date
        elif any(word in user_lower for word in ['date', 'today', 'what day']):
            current_date = date.today().strftime('%A, %B %d, %Y')
            return f"📅 Today is {current_date}"
        
        # Jokes
        elif any(word in user_lower for word in ['joke', 'funny', 'laugh']):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything! 😄",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
                "Why don't eggs tell jokes? They'd crack each other up! 🥚",
                "What do you call a fake noodle? An impasta! 🍝",
                "Why did the math book look so sad? Because it had too many problems! 📚"
            ]
            return random.choice(jokes)
        
        # Math
        elif any(word in user_lower for word in ['calculate', 'math', '+', '-', '*', '/']):
            try:
                if '+' in user_message:
                    parts = user_message.split('+')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        return f"🧮 {a} + {b} = {a + b}"
                elif '-' in user_message:
                    parts = user_message.split('-')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        return f"🧮 {a} - {b} = {a - b}"
                elif '*' in user_message:
                    parts = user_message.split('*')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        return f"🧮 {a} × {b} = {a * b}"
                elif '/' in user_message:
                    parts = user_message.split('/')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        if b != 0:
                            return f"🧮 {a} ÷ {b} = {a / b}"
                        else:
                            return "❌ Cannot divide by zero!"
            except:
                return "Try: 'calculate 5 + 3' or 'what is 10 * 2'"
        
        # Help
        elif any(word in user_lower for word in ['help', 'what can you do']):
            return """🤖 I can help you with:
• Telling time ⏰
• Date information 📅  
• Funny jokes 😄
• Basic math calculations 🧮
• General chatting 💬

Try: 'what time is it', 'tell me a joke', or 'calculate 8 * 7'"""
        
        # Goodbye
        elif any(word in user_lower for word in ['bye', 'goodbye', 'exit']):
            return "Goodbye! Thanks for chatting! 👋"
        
        # Default response
        else:
            responses = [
                "That's interesting! Tell me more! 💭",
                "I'm listening! What would you like to know? 🤔",
                "I can tell you the time, date, share a joke, or do math! What would you like? 🌟",
                "Hmm, that's cool! Ask me about the time or for a joke! 😊"
            ]
            return random.choice(responses)

def main():
    print(f"{Fore.CYAN}")
    print("╔══════════════════════════════════════════════════╗")
    print("║               🤖 SIMPLE CHATBOT 🤖              ║")
    print("║                  (No Internet Needed)           ║")
    print("╚══════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)
    
    bot = SimpleChatBot("Chatty")
    
    print(f"{Fore.GREEN}Ready to chat! Type 'quit' to exit.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Try: 'what time is it', 'tell me a joke', 'calculate 5+3'{Style.RESET_ALL}\n")
    
    while True:
        try:
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print(f"{Fore.GREEN}Bot: Goodbye! 👋{Style.RESET_ALL}")
                break
            
            if not user_input:
                continue
            
            response = bot.get_response(user_input)
            print(f"{Fore.GREEN}Bot: {Style.RESET_ALL}{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}Bot: Goodbye! 👋{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
