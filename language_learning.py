import random

words = [
    {"jp": "こんにちは", "romaji": "konnichiwa", "en": "Hello"},
    {"jp": "ありがとう", "romaji": "arigatou", "en": "Thank you"},
    {"jp": "さようなら", "romaji": "sayounara", "en": "Goodbye"},
    {"jp": "はい", "romaji": "hai", "en": "Yes"},
    {"jp": "いいえ", "romaji": "iie", "en": "No"},
    {"jp": "おはよう", "romaji": "ohayou", "en": "Good morning"},
    {"jp": "こんばんは", "romaji": "konbanwa", "en": "Good evening"},
    {"jp": "おやすみ", "romaji": "oyasumi", "en": "Good night"},
    {"jp": "すみません", "romaji": "sumimasen", "en": "Excuse me"},
    {"jp": "ごめんなさい", "romaji": "gomennasai", "en": "I'm sorry"},
    {"jp": "わかりません", "romaji": "wakarimasen", "en": "I don't understand"},
    {"jp": "わかります", "romaji": "wakarimasu", "en": "I understand"},
    {"jp": "なまえ", "romaji": "namae", "en": "Name"},
    {"jp": "ともだち", "romaji": "tomodachi", "en": "Friend"},
    {"jp": "がくせい", "romaji": "gakusei", "en": "Student"},
    {"jp": "せんせい", "romaji": "sensei", "en": "Teacher"},
    {"jp": "いえ", "romaji": "ie", "en": "House"},
    {"jp": "へや", "romaji": "heya", "en": "Room"},
    {"jp": "くるま", "romaji": "kuruma", "en": "Car"},
    {"jp": "でんしゃ", "romaji": "densha", "en": "Train"},
    {"jp": "えき", "romaji": "eki", "en": "Station"},
    {"jp": "みせ", "romaji": "mise", "en": "Shop"},
    {"jp": "たべもの", "romaji": "tabemono", "en": "Food"},
    {"jp": "のみもの", "romaji": "nomimono", "en": "Drink"},
    {"jp": "みず", "romaji": "mizu", "en": "Water"},
    {"jp": "ごはん", "romaji": "gohan", "en": "Rice"},
    {"jp": "ごはん", "romaji": "gohan", "en": "Meal"},
    {"jp": "にく", "romaji": "niku", "en": "Meat"},
    {"jp": "やさい", "romaji": "yasai", "en": "Vegetables"},
    {"jp": "さかな", "romaji": "sakana", "en": "Fish"},
    {"jp": "くだもの", "romaji": "kudamono", "en": "Fruit"},
    {"jp": "パン", "romaji": "pan", "en": "Bread"},
    {"jp": "コーヒー", "romaji": "koohii", "en": "Coffee"},
    {"jp": "おちゃ", "romaji": "ocha", "en": "Tea"},
    {"jp": "あさ", "romaji": "asa", "en": "Morning"},
    {"jp": "ひる", "romaji": "hiru", "en": "Noon"},
    {"jp": "よる", "romaji": "yoru", "en": "Night"},
    {"jp": "きょう", "romaji": "kyou", "en": "Today"},
    {"jp": "あした", "romaji": "ashita", "en": "Tomorrow"},
    {"jp": "きのう", "romaji": "kinou", "en": "Yesterday"},
    {"jp": "いま", "romaji": "ima", "en": "Now"},
    {"jp": "とき", "romaji": "toki", "en": "Time"},
    {"jp": "ひと", "romaji": "hito", "en": "Person"},
    {"jp": "おとこ", "romaji": "otoko", "en": "Man"},
    {"jp": "おんな", "romaji": "onna", "en": "Woman"},
    {"jp": "こども", "romaji": "kodomo", "en": "Child"},
    {"jp": "かぞく", "romaji": "kazoku", "en": "Family"},
    {"jp": "ちち", "romaji": "chichi", "en": "Father"},
    {"jp": "はは", "romaji": "haha", "en": "Mother"},
    {"jp": "あに", "romaji": "ani", "en": "Older brother"},
    {"jp": "あね", "romaji": "ane", "en": "Older sister"},
    {"jp": "おとうと", "romaji": "otouto", "en": "Younger brother"},
    {"jp": "いもうと", "romaji": "imouto", "en": "Younger sister"},
    {"jp": "いぬ", "romaji": "inu", "en": "Dog"},
    {"jp": "ねこ", "romaji": "neko", "en": "Cat"},
    {"jp": "とり", "romaji": "tori", "en": "Bird"},
    {"jp": "て", "romaji": "te", "en": "Hand"},
    {"jp": "あし", "romaji": "ashi", "en": "Leg / Foot"},
    {"jp": "め", "romaji": "me", "en": "Eye"},
    {"jp": "みみ", "romaji": "mimi", "en": "Ear"},
    {"jp": "くち", "romaji": "kuchi", "en": "Mouth"},
    {"jp": "はな", "romaji": "hana", "en": "Nose"},
    {"jp": "ここ", "romaji": "koko", "en": "Here"},
    {"jp": "そこ", "romaji": "soko", "en": "There"},
    {"jp": "あそこ", "romaji": "asoko", "en": "Over there"},
    {"jp": "どこ", "romaji": "doko", "en": "Where"},
    {"jp": "なに", "romaji": "nani", "en": "What"},
    {"jp": "だれ", "romaji": "dare", "en": "Who"},
    {"jp": "なぜ", "romaji": "naze", "en": "Why"},
    {"jp": "いつ", "romaji": "itsu", "en": "When"},
    {"jp": "いくら", "romaji": "ikura", "en": "How much"},
    {"jp": "いくつ", "romaji": "ikutsu", "en": "How many"},
    {"jp": "すき", "romaji": "suki", "en": "Like"},
    {"jp": "きらい", "romaji": "kirai", "en": "Dislike"},
    {"jp": "たのしい", "romaji": "tanoshii", "en": "Fun"},
    {"jp": "うれしい", "romaji": "ureshii", "en": "Happy"},
    {"jp": "かなしい", "romaji": "kanashii", "en": "Sad"},
    {"jp": "こわい", "romaji": "kowai", "en": "Scary"},
    {"jp": "つかれた", "romaji": "tsukareta", "en": "Tired"},
    {"jp": "たいせつ", "romaji": "taisetsu", "en": "Important"},
    {"jp": "たかい", "romaji": "takai", "en": "Expensive"},
    {"jp": "たかい", "romaji": "takai", "en": "Tall"},
    {"jp": "やすい", "romaji": "yasui", "en": "Cheap"},
    {"jp": "おおきい", "romaji": "ookii", "en": "Big"},
    {"jp": "ちいさい", "romaji": "chiisai", "en": "Small"},
    {"jp": "ながい", "romaji": "nagai", "en": "Long"},
    {"jp": "みじかい", "romaji": "mijikai", "en": "Short"},
    {"jp": "はやい", "romaji": "hayai", "en": "Fast"},
    {"jp": "おそい", "romaji": "osoi", "en": "Slow"},
    {"jp": "あたらしい", "romaji": "atarashii", "en": "New"},
    {"jp": "ふるい", "romaji": "furui", "en": "Old"},
    {"jp": "きれい", "romaji": "kirei", "en": "Beautiful"},
    {"jp": "きれい", "romaji": "kirei", "en": "Clean"},
    {"jp": "よごれた", "romaji": "yogoreta", "en": "Dirty"},
    {"jp": "あつい", "romaji": "atsui", "en": "Hot"},
    {"jp": "さむい", "romaji": "samui", "en": "Cold"},
    {"jp": "げんき", "romaji": "genki", "en": "Healthy"},
    {"jp": "げんき", "romaji": "genki", "en": "Energetic"},
    {"jp": "びょうき", "romaji": "byouki", "en": "Sick"},
    {"jp": "いく", "romaji": "iku", "en": "To go"},
    {"jp": "くる", "romaji": "kuru", "en": "To come"},
    {"jp": "たべる", "romaji": "taberu", "en": "To eat"},
    {"jp": "のむ", "romaji": "nomu", "en": "To drink"},
    {"jp": "みる", "romaji": "miru", "en": "To see"},
    {"jp": "みる", "romaji": "miru", "en": "To watch"},
    {"jp": "きく", "romaji": "kiku", "en": "To listen"},
    {"jp": "きく", "romaji": "kiku", "en": "To ask"},
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['jp']} {word['romaji']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['en'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['en']}.\n")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz. . .")
    quiz_user(words)

if __name__ == "__main__":
    main()