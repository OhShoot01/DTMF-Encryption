import sounddevice as sd
import numpy as np
import time
import random

randomness_key = None

def create_randomness_key():
    print("Create a randomness key by entering a series of unique characters without spaces.")
    key = input("Enter the randomness key: ")
    return key

if randomness_key is None:
    randomness_key = create_randomness_key()

while True:
    def play_dtmf_tone(digit):
        dtmf_frequencies = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '0': (941, 1336), '*': (941, 1209), '#': (941, 1477), ' ': (990, 1209)
    }
    
        if digit.upper() in dtmf_frequencies:
            frequency1, frequency2 = dtmf_frequencies[digit.upper()]
    
            # Set the duration and sample rate
            duration = 0.1  # in seconds
            sample_rate = 44100
    
            # Generate samples for the two frequencies
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            tone1 = 0.5 * np.sin(2 * np.pi * frequency1 * t)
            tone2 = 0.5 * np.sin(2 * np.pi * frequency2 * t)
    
            # Combine the two tones
            tone = tone1 + tone2
    
            # Play the tone
            sd.play(tone, sample_rate)
            sd.wait()


    

    def apply_randomness_algorithm(char, randomness_key):
        random.seed(ord(char) + len(randomness_key))
        characters = '0123456789#* '
        return random.choice(characters)

    def transform_prompt(prompt, randomness_key):
        result = ""
        for char in prompt:
            randomness_values = apply_randomness_algorithm(char, randomness_key)
            result += f"{randomness_values}"
    
        return result.strip()
    
    def main():
        user_prompt = input("Enter your prompt: ")
        
        transformed_prompt = transform_prompt(user_prompt, randomness_key)
           
        print("\nFinal Result:")
        print(transformed_prompt)
        print()
        
        for digit in transformed_prompt:
            play_dtmf_tone(digit)
            time.sleep(0.13)
    
    if __name__ == "__main__":
        main()
