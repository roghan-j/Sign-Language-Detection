from gtts import gTTS
import os
import time

sentence= [
    ["hello", "need", "talk", "you", "about", "health"],
    ["hello", "need", "talk", "you", "about", "health"],
    ["about", "need", "talk", "hello", "about", "health"],
    ["hello", "talk", "talk", "you", "about", "hello"],
    ["feel", "sick", "cold", "my", "sick"],
    ["feel", "sick", "cold", "my", "have"],
    ["cold", "sick", "cold", "sick", "have"],
    ["feel", "sick", "cold", "my", "feel"],
]

for i in sentence:
    filename= "./voice/voice-"+str(time.time())+".mp3"
    gTTS(text=" ".join(i), lang="en", slow=True).save(filename)