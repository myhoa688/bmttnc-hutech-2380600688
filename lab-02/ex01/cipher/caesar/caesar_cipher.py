from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        if not isinstance(key, int):
            raise ValueError("Key must be an integer.")
        if key % 26 == 0:
            raise ValueError("Key must not be 0 or a multiple of 26.")
        key = key % 26
        encrypted_text = []
        for letter in text:
            if letter.isupper():
                if letter in self.alphabet:
                    letter_index = self.alphabet.index(letter)
                    output_index = (letter_index + key) % len(self.alphabet)
                    output_letter = self.alphabet[output_index]
                    encrypted_text.append(output_letter)
                else:
                    encrypted_text.append(letter)
            elif letter.islower():
                upper_letter = letter.upper()
                if upper_letter in self.alphabet:
                    letter_index = self.alphabet.index(upper_letter)
                    output_index = (letter_index + key) % len(self.alphabet)
                    output_letter = self.alphabet[output_index].lower()
                    encrypted_text.append(output_letter)
                else:
                    encrypted_text.append(letter)
            else:
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        if not isinstance(key, int):
            raise ValueError("Key must be an integer.")
        if key % 26 == 0:
            raise ValueError("Key must not be 0 or a multiple of 26.")
        key = key % 26
        decrypted_text = []
        for letter in text:
            if letter.isupper():
                if letter in self.alphabet:
                    letter_index = self.alphabet.index(letter)
                    output_index = (letter_index - key) % len(self.alphabet)
                    output_letter = self.alphabet[output_index]
                    decrypted_text.append(output_letter)
                else:
                    decrypted_text.append(letter)
            elif letter.islower():
                upper_letter = letter.upper()
                if upper_letter in self.alphabet:
                    letter_index = self.alphabet.index(upper_letter)
                    output_index = (letter_index - key) % len(self.alphabet)
                    output_letter = self.alphabet[output_index].lower()
                    decrypted_text.append(output_letter)
                else:
                    decrypted_text.append(letter)
            else:
                decrypted_text.append(letter)
        return "".join(decrypted_text)