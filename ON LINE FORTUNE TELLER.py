# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:49:33 2024

FORTUNE TELLER - ON LINE FORTUNE TELLER -

OZZRORO   ROZO WITH Z.

@author: rober ugalde
"""

https://obriolimited.teamtailor.com/schedule/98e5cbd1-5aec-4b70-bb6e-fa4f4a994755

TEAMTAILOR  - JOIN MEETING.

DMYTRO MAKHYNA  - Interviewer.

TUESDAY 10 DECEM

7.00 AM  7.15 AM  CST.

https://app.teamtailor.com/video-meetings/67d3f518-0d9f-4780-b0a3-a56c33af3b7d


10-12-2024.   15:00 to 15:45  EET.

that is 7.00 to 7.45 CST --

good luck




import random

# Define the Tarot card deck (78 cards with their names)
tarot_cards = [
    "0 - The Fool", "1 - The Magician", "2 - The High Priestess", "3 - The Empress",
    "4 - The Emperor", "5 - The Hierophant", "6 - The Lovers", "7 - The Chariot",
    "8 - Strength", "9 - The Hermit", "10 - Wheel of Fortune", "11 - Justice",
    "12 - The Hanged Man", "13 - Death", "14 - Temperance", "15 - The Devil",
    "16 - The Tower", "17 - The Star", "18 - The Moon", "19 - The Sun",
    "20 - Judgement", "21 - The World"
] + [f"{i + 22} - {suit} {rank}" for suit in ["Cups", "Pentacles", "Swords", "Wands"] for rank in [
    "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"
]]

def tarot_reading():
    print("Welcome to the Tarot Prediction Chat!")
    print("Think about your question, then choose a number between 1 and 78 for your current situation.")
    
    # Ask user for their chosen number
    while True:
        try:
            user_choice = int(input("Enter your number (1-78): "))
            if 1 <= user_choice <= 78:
                break
            else:
                print("Please enter a number between 1 and 78.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 78.")
    
    # Get the Tarot card for the user's current situation
    current_card = tarot_cards[user_choice - 1]
    
    # Generate a random Tarot card for the future
    future_card_index = random.randint(1, 78)
    while future_card_index == user_choice:
        future_card_index = random.randint(1, 78)  # Ensure future card is different
    future_card = tarot_cards[future_card_index - 1]
    
    # Display the reading
    print("\n--- Tarot Reading ---")
    print(f"Your current situation: Card {user_choice} - {current_card}")
    print(f"For your future: Card {future_card_index} - {future_card}")
    print("----------------------")
    print("Thank you for visiting the Tarot Chat! Reflect on this and take care.")

# Run the Tarot reading chat
if __name__ == "__main__":
    tarot_reading()





xxxxxxxx



import random

# Define the Tarot card deck (78 cards with their names)
tarot_cards = [
    "0 - The Fool", "1 - The Magician", "2 - The High Priestess", "3 - The Empress",
    "4 - The Emperor", "5 - The Hierophant", "6 - The Lovers", "7 - The Chariot",
    "8 - Strength", "9 - The Hermit", "10 - Wheel of Fortune", "11 - Justice",
    "12 - The Hanged Man", "13 - Death", "14 - Temperance", "15 - The Devil",
    "16 - The Tower", "17 - The Star", "18 - The Moon", "19 - The Sun",
    "20 - Judgement", "21 - The World"
] + [f"{22 + index} - {suit} {rank}" for index, (suit, rank) in enumerate(
    [(suit, rank) for suit in ["Cups", "Pentacles", "Swords", "Wands"]
     for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]]
)]

def tarot_reading():
    print("Welcome to the Tarot Prediction Chat!")
    print("Think about your question, then choose a number between 1 and 78 for your current situation.")
    
    # Ask user for their chosen number
    while True:
        try:
            user_choice = int(input("Enter your number (1-78): "))
            if 1 <= user_choice <= 78:
                break
            else:
                print("Please enter a number between 1 and 78.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 78.")
    
    # Get the Tarot card for the user's current situation
    current_card = tarot_cards[user_choice - 1]
    
    # Generate a random Tarot card for the future
    future_card_index = random.randint(1, 78)
    while future_card_index == user_choice:
        future_card_index = random.randint(1, 78)  # Ensure future card is different
    future_card = tarot_cards[future_card_index - 1]
    
    # Display the reading
    print("\n--- Tarot Reading ---")
    print(f"Your current situation: Card {user_choice} - {current_card}")
    print(f"For your future: Card {future_card_index} - {future_card}")
    print("----------------------")
    print("Thank you for visiting the Tarot Chat! Reflect on this and take care.")

# Run the Tarot reading chat
if __name__ == "__main__":
    tarot_reading()


xxxxxXXXXXX

improved situation.


--- Tarot Reading ---
Your current situation: Card 13 - Death
Meaning: Endings, change, transformation, transition.

For your future: Card 45 - Pentacles King
Meaning: Card from the Pentacles suit representing king in life.
----------------------


import random

# Define the Tarot card deck (78 cards with their names and meanings)
tarot_cards = [
    {"name": "0 - The Fool", "meaning": "New beginnings, innocence, spontaneity, a free spirit."},
    {"name": "1 - The Magician", "meaning": "Manifestation, resourcefulness, power, inspired action."},
    {"name": "2 - The High Priestess", "meaning": "Intuition, sacred knowledge, divine feminine, the subconscious mind."},
    {"name": "3 - The Empress", "meaning": "Femininity, beauty, nature, nurturing, abundance."},
    {"name": "4 - The Emperor", "meaning": "Authority, structure, control, fatherhood."},
    {"name": "5 - The Hierophant", "meaning": "Spiritual wisdom, religious beliefs, tradition, conformity."},
    {"name": "6 - The Lovers", "meaning": "Love, harmony, partnerships, choices, values alignment."},
    {"name": "7 - The Chariot", "meaning": "Control, willpower, success, determination."},
    {"name": "8 - Strength", "meaning": "Courage, persuasion, influence, compassion."},
    {"name": "9 - The Hermit", "meaning": "Soul-searching, introspection, being alone, inner guidance."},
    {"name": "10 - Wheel of Fortune", "meaning": "Good luck, karma, life cycles, destiny, a turning point."},
    {"name": "11 - Justice", "meaning": "Justice, fairness, truth, cause and effect, law."},
    {"name": "12 - The Hanged Man", "meaning": "Pause, surrender, letting go, new perspectives."},
    {"name": "13 - Death", "meaning": "Endings, change, transformation, transition."},
    {"name": "14 - Temperance", "meaning": "Balance, moderation, patience, purpose."},
    {"name": "15 - The Devil", "meaning": "Shadow self, attachment, addiction, restriction."},
    {"name": "16 - The Tower", "meaning": "Sudden change, upheaval, chaos, revelation."},
    {"name": "17 - The Star", "meaning": "Hope, faith, purpose, renewal, spirituality."},
    {"name": "18 - The Moon", "meaning": "Illusion, fear, anxiety, subconscious, intuition."},
    {"name": "19 - The Sun", "meaning": "Positivity, fun, warmth, success, vitality."},
    {"name": "20 - Judgement", "meaning": "Judgement, rebirth, inner calling, absolution."},
    {"name": "21 - The World", "meaning": "Completion, integration, accomplishment, travel."}
] + [
    {"name": f"{22 + index} - {suit} {rank}", "meaning": f"Card from the {suit} suit representing {rank.lower()} in life."}
    for index, (suit, rank) in enumerate(
        [(suit, rank) for suit in ["Cups", "Pentacles", "Swords", "Wands"]
         for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]]
    )
]

def tarot_reading():
    print("Welcome to the Tarot Prediction Chat!")
    print("Think about your question, then choose a number between 1 and 78 for your current situation.")
    
    # Ask user for their chosen number
    while True:
        try:
            user_choice = int(input("Enter your number (1-78): "))
            if 1 <= user_choice <= 78:
                break
            else:
                print("Please enter a number between 1 and 78.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 78.")
    
    # Get the Tarot card for the user's current situation
    current_card = tarot_cards[user_choice - 1]
    
    # Generate a random Tarot card for the future
    future_card_index = random.randint(1, 78)
    while future_card_index == user_choice:
        future_card_index = random.randint(1, 78)  # Ensure future card is different
    future_card = tarot_cards[future_card_index - 1]
    
    # Display the reading
    print("\n--- Tarot Reading ---")
    print(f"Your current situation: Card {user_choice} - {current_card['name']}")
    print(f"Meaning: {current_card['meaning']}")
    print()
    print(f"For your future: Card {future_card_index} - {future_card['name']}")
    print(f"Meaning: {future_card['meaning']}")
    print("----------------------")
    print("Thank you for visiting the Tarot Chat! Reflect on this and take care.")

# Run the Tarot reading chat
if __name__ == "__main__":
    tarot_reading()








