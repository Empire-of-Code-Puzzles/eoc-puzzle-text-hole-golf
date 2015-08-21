You are given a chunk of text as a sequence of strings. 
If we place them in columns in the order of how they are given,
then we get an 2D array with various row lengths.
A plot hole is a single white-space surrounded by letters,
digits or punctuation symbols - up, down, left, right and diagonally.
Two or more spaces do not constitute a plot hole.
All `"outer"` characters a consider white-spaces, so a space on the outside cannot be considered a plot hole.
Your goal is count the number of plot holes in the given text.

Let's look an example:

```
How are you doing?
I'm fine. OK.
Lorem Ipsum?
Of course!!!
1234567890
0        0
1234567890
Fine! good buy!
```

Here we can find three plot holes: before `"OK"`; between `"Lorem"` and `"Ipsum"`; inside `"Of course!!!"`.
