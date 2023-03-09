import speech_recognition as sr


r = sr.Recognizer()
with sr.AudioFile('audiomass-output-10min.wav') as source:
    audio_data = r.record(source)

# Convert the audio data to text
text = r.recognize_google(audio_data,
                          language="id",
                          show_all=False)

# Print the text to the terminal
print(text)

# Save the recognized text as a text file
with open('recognized_text.txt', 'w') as file:
    file.write(text)

# Print a success message
print(f"Recognized text saved to recognized_text.txt")
