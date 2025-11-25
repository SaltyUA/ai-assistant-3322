import random
import os

NAME = "Jarvis"
PERSONALITY_FILE = "persona.txt"
PERSONALITY_DEFAULT = "Дружній"

def load_persona(filename=PERSONALITY_FILE):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception:
            pass    
    return PERSONALITY_DEFAULT  


PERSONALITY = load_persona()

greatings = ["Привіт", "Хай", "Вітаю"]

def random_greating():
    return random.choice(greatings)

def get_response(text):
    return f"{NAME}(: Я отримав твоє повідомлення - '{text}'"

def main():
    print(PERSONALITY)
    print(f"{NAME}: {random_greating()}! Готовий працювати. Якщо хочеш вийти напиши 'exit'")
    while True:
        user = input("Ти: ")
        if user in "exit":
            print(f"{NAME}: Бувай!")
            break
        print(get_response(user))
        
if __name__ == "__main__":
    main()        