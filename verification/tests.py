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
            "input": ['Lorem ipsum dolor', 'sit amet,', 'consectetuer', 'adipiscing elit.', 'Aenean commodo',
                      'ligula eget dolor.', 'Aenean massa. Cum', 'sociis natoque', 'penatibus et magnis',
                      'dis parturient', 'montes, nascetur', 'ridiculus mus. Donec', 'quam felis,', 'ultricies nec,',
                      'pellentesque eu,', 'pretium quis, sem.', 'Nulla consequat', 'massa quis enim.',
                      'Donec pede justo,', 'fringilla vel,'],
            "answer": 11,
            "explanation": [[1, 3], [3, 10], [5, 11], [8, 9], [8, 12], [9, 3], [10, 7], [11, 9], [12, 4], [13, 9],
                            [15, 7]]
        },
        {
            "input": ['qwerty asdfg ghjkl 123'],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1',
                      'asd', '0 1', 'asd', '0 1', 'asd', '0 1'],
            "answer": 9,
            "explanation": [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1], [11, 1], [13, 1], [15, 1], [17, 1]]
        },
        {
            "input": ['hi hi', 'hello', 'hello', 'hello', 'hello', 'hello', 'by by'],
            "answer": 0,
            "explanation": []
        },
        {
            "input": [' X ', 'XXX', ' X ', 'X X', ' X '],
            "answer": 0,
            "explanation": []
        },
    ]
}
