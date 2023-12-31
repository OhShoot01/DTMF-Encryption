import numpy as np
import time
import pyaudio
import random
import DTMF2

CHUNK = 16000
RATE = 44100

p = pyaudio.PyAudio()

last_activity_time = time.time()
new_line_started = False

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)

randomness_key = None

def create_randomness_key():
    print("Create a randomness key by entering a series of unique characters without spaces.")
    key = input("Enter the randomness key: ")
    return key

if randomness_key is None:
    randomness_key = create_randomness_key()

while True:
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    new_res = DTMF2.DTMF(data, RATE)

    if new_res != "":
        if not new_line_started:
            # Start a new line if it hasn't been started
            print()
            new_line_started = True

        # Print in one single line
        print(new_res, end=' ')
        
        # Update the last activity time
        last_activity_time = time.time()
    else:
        # Check for inactivity after 5 seconds
        if time.time() - last_activity_time > 3 and new_line_started:
            print()  # Start a new line after 3 seconds of inactivity
            new_line_started = False
            
    
    
    def reverse_randomness_algorithm(encrypted_char, randomness_key):
        random.seed(ord(encrypted_char) + len(randomness_key))
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#* '
    
    # To decipher, we need to find the index of the encrypted_char in the characters list
    encrypted_index = characters.index(encrypted_char)
    
    # Reverse the randomness algorithm by generating the original character at that index
    original_char = characters[encrypted_index]
    
    return original_char

    def decipher_text(encrypted_text, randomness_key):
        decrypted_text = ''
        for char in encrypted_text:
            decrypted_char = reverse_randomness_algorithm(char, randomness_key)
            decrypted_text += decrypted_char
        return decrypted_text

    # Example usage:
    encrypted_text = new_res  # Replace with your encrypted text
    decrypted_text = decipher_text(encrypted_text, randomness_key)
    print("Decrypted Text:", decrypted_text)
