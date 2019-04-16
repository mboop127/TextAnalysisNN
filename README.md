# TextAnalysisNN
A basic but very complex NN that reads texts and produces analysis

How to run:

Currently this will read Shakespeare and produce 25 words based on a random 100 character passage of Shakespeare's sonnets.

Place all files in a folder together.

If you want to change the input:
1.) Open 1.txt and delete everything. Replace it with text of any length. Be sure to remove all "'"s, and most line breaks. It will not run if there are any apostrophes.
2.) Run parser.py
>>>Do not run parser.py more than once! It will overwrite the first file and corrupt the data.

If you want to change the output length:
1.) Open ShakespeareNN.py
2.) Edit the "OutputLength = 25" to equal any value you like. Note: the smaller the number, the more input data will be lost.

When you run ShakespeareNN.py it will prompt you to input "a" or "d." If you think the words produced are good (at least relative to the others), hit "a." If not hit "d."
After a long period of time it should evolve according to your feedback.

You can add or remove words form the wordlist file in order to remove or add them to the dictionary, just be sure to maintain the formatting.

Every 10th successful ("a") phrase will be saved to your directory. You should be able to see progress over time.

Email m.boop127@gmail.com with any questions/suggestions.
