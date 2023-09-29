# Morse-Code
Development of a Morse Code Translation and Communication Platform


Morse Code:
- Morse Code uses different combinations "dot" (.) and "dash" (-) to encode 26 letters (A-Z) and 10 numbers (0-9)
- It is usuall conveyed in the form of light or sound waves, but telegraphy also made it possible to transfer through telecomm



What the app does:
- Translate text to Morse and vice versa


What widgets are needed:
- A button to toggle translation mode (Text -> Morse or Morse -> Text)
- An entry field which receive input from user (Either text or Morse) and allows user to copy/paste
- An output field which displays output after translation and allows user to copy/paste


What 


Basic Tasks
1. Create a GUI which has an entry field and display field aligned vertically
2. Create a Morse Code dictionary
3. Add functions to receive inputs, translate, and display outputs


Advanced Tasks
1. Add functions in GUI which allow user to save and open previously translated codes or texts as files
2. 


Challenges:
1. How to receive "dot and dash" input from user if I don't use 0 and 1?
2. How to time the dot, dash, and off times
3. 




### WIDGETS ###

# Input field

# Output field

# Buttons
1. "Translate": Pass the input to the translation function and then activate display function
2. "Save": Save the input AND output as a file and show in the files column
3. "Delete": Delete the selected saved file(s)

# Functions
- Timer: count time during which the key is held down or lifted
- Pattern recognition: 

### Timing ###

Dot:            . (unit time)
Dash:           - (3 times longer than Dot)
Symbol space:   time between dots or dashes within the same charater
Letter space:   time between characters (mulitple of which form a word)
Word space:     time between words
So there needs to be a timer function which keep track of the time during which the key is pressed and released

