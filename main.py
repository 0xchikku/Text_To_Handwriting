import pywhatkit

#handwriting function which converts text to handwriting
def handwriting(text):
    pywhatkit.text_to_handwriting(text)
    #a .txt file and an Image with .png extension will be saved in the same folder 


# getting input from user
text = input('Enter or Paste the Text here: ')

#calling the handwriting function and passing input text as argument
handwriting(text)