import pyttsx3
engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')       #getting details of current voice
# print("total voices:",voices)
def tts(text,output_prefix,rate=125,volume=1.0,voice=0):
    engine.setProperty('rate', rate)     # setting up new voice rate
    engine.setProperty('volume',volume)    # setting up volume level  between 0 and 18
    engine.setProperty('voice', voices[voice].id)   
    engine.save_to_file(text, '{}.mp3'.format(output_prefix))
    engine.runAndWait()
