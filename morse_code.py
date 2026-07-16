import streamlit as st
eng_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

# Morse -> English
morse_to_eng = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",}
message = st.text_input("What is your message?",help="Your message can be either in english or morse code.")
final_message = ""
if '-' in message:
    current_word = ""
    for char in message:
        if char != " ":
            current_word += char
        else:
            current_word = morse_to_eng[current_word]
            final_message += f' {current_word}'
            current_word = ""
    st.write(f"Your message is {final_message}")
else:
    current_word = ""
    for char in message:
        if char != " ":
            current_word += char
        else:
            current_word = morse_to_eng[current_word]
            final_message += f' {current_word}'
            current_word = ""
    st.write(f"Your message is {final_message}")