"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["How are you doing?",
                      "I'm fine. OK.",
                      "Lorem Ipsum?",
                      "Of course!!!",
                      "1234567890",
                      "0        0",
                      "1234567890",
                      "Fine! good buy!"],
            "answer": 3,
            "explanation": [[1, 9], [2, 5], [3, 2]],
        },
        {
            "input": ["WoW",
                      "A A",
                      "WoW"],
            "answer": 1,
            "explanation": [[1, 1]]
        },
        {
            "input": ["HELLO",
                      "O O O",
                      "NIGHT",
                      "O O O",
                      "IDDQD"],
            "answer": 4,
            "explanation": [[1, 1], [1, 3], [3, 1], [3, 3]]
        },
        {
            "input": ["HELLO",
                      "O   O",
                      "NIGHT",
                      "O   O",
                      "IDDQD"],
            "answer": 0,
            "explanation": []
        },



    ],
    "Extra": [
        {
            "input": ["How are you doing?",
                      "I'm fine. OK.",
                      "Lorem Ipsum?",
                      "Of course!!!",
                      "1234567890",
                      "0        0",
                      "1234567890",
                      "Fine! good buy!"],
            "answer": 3,
            "explanation": [[1, 9], [2, 5], [3, 2]],
        },
        {
            "input": ["WoW",
                      "A A",
                      "WoW"],
            "answer": 1,
            "explanation": [[1, 1]]
        },
        {
            "input": ["HELLO",
                      "O O O",
                      "NIGHT",
                      "O O O",
                      "IDDQD"],
            "answer": 4,
            "explanation": [[1, 1], [1, 3], [3, 1], [3, 3]]
        },
        {
            "input": ["HELLO",
                      "O   O",
                      "NIGHT",
                      "O   O",
                      "IDDQD"],
            "answer": 0,
            "explanation": []
        },
    ]
}
