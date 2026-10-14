#wingdings translator
alphabet = 'abcdefghijklmnopqrstuvwxyz'
wingdings_lower = '✌👌👍👎👈👉☝👇🖐☺😐☹💣☠🏳🏴✈✉🖃🖄🖅🖆📂📄🗏🗎'
wingdings_upper = '♋♋︎♌︎♍︎♎︎♏︎♐︎♑︎♒︎♓︎🙰🙵●︎❍︎■︎□︎◻︎❑︎❒︎⬧︎⧫︎◆︎❖︎⬥︎⌧︎⍓︎⌘︎'

def alphabet_to_wingdings(text):
  for letter in text:
    if letter in '~!@#$%^&*()':
      print(letter, end='')
    elif letter.lower() in alphabet:
      letter_placement = ord(letter.lower()) - ord('a')
      if letter.isupper():
        print(wingdings_upper[letter_placement], end='')
      else:
        print(wingdings_lower[letter_placement], end='')
    else:
      print(letter, end='')
text = 'Hello'
#alphabet_to_wingdings(text)
print(len(wingdings_upper))
