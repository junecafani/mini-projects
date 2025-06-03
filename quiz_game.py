

questions = [
    {
        "prompt": "Apa ibu kota negara Indonesia?",
        "options": ["A. Jakarta", "B. Surabaya", "C. Yogyakarta", "D. Bandung"],
        "answer": "A"
    },
    {
        "prompt": "Siapa presiden pertama Republik Indonesia?",
        "options": ["A. Joko Widodo", "B. Soekarno", "C. Soeharto", "D. B.J. Habibie"],
        "answer": "B"
    },
    {
        "prompt": "Pulau manakah yang paling padat penduduknya di Indonesia?",
        "options": ["A. Sumatera", "B. Kalimantan", "C. Sulawesi", "D. Jawa"],
        "answer": "D"
    },
    {
        "prompt": "Apa nama lagu kebangsaan Indonesia?",
        "options": ["A. Rayuan Pulau Kelapa", "B. Indonesia Tanah Air Beta", "C. Indonesia Raya", "D. Bagimu Negeri"],
        "answer": "C"
    },
    {
        "prompt": "Kapan Indonesia memproklamasikan kemerdekaannya?",
        "options": ["A. 17 Agustus 1945", "B. 20 Mei 1908", "C. 10 November 1945", "D. 1 Juni 1945"],
        "answer": "A"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong, LOSERR!!! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} question correct.")

run_quiz(questions)