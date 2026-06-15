class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        if not isinstance(key, str) or not key or not key.isalpha():
            raise ValueError("Key must be a non-empty string containing only alphabetic characters (no numbers, spaces, or special characters).")
        key = key.upper().replace("J", "I")
        seen = set()
        matrix = []
        for letter in key:
            if letter.isalpha() and letter not in seen:
                seen.add(letter)
                matrix.append(letter)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in seen:
                seen.add(letter)
                matrix.append(letter)
                if len(matrix) == 25:
                    break
        
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào, giữ lại chỉ các ký tự chữ cái
        clean_text = ""
        for char in plain_text.upper():
            if char.isalpha():
                if char == 'J':
                    clean_text += 'I'
                else:
                    clean_text += char

        # Chia thành các cặp (digraphs), xử lý trùng lặp và độ dài lẻ
        pairs = []
        i = 0
        while i < len(clean_text):
            char1 = clean_text[i]
            if i + 1 < len(clean_text):
                char2 = clean_text[i+1]
                if char1 == char2:
                    filler = 'Q' if char1 == 'X' else 'X'
                    pairs.append(char1 + filler)
                    i += 1
                else:
                    pairs.append(char1 + char2)
                    i += 2
            else:
                filler = 'Q' if char1 == 'X' else 'X'
                pairs.append(char1 + filler)
                i += 1

        encrypted_text = ""
        for pair in pairs:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        # Clean cipher text (keep only alphabetical characters, uppercase)
        cipher_text = "".join([c.upper() for c in cipher_text if c.isalpha()])
        if not cipher_text:
            return ""

        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            if len(pair) < 2:
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        banro = ""
        # Reconstruct original plaintext (remove filler characters X or Q)
        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i+2] and decrypted_text[i+1] in ('X', 'Q'):
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i+1]

        if len(decrypted_text) >= 2:
            last_pair = decrypted_text[-2:]
            if last_pair[1] in ('X', 'Q'):
                banro += last_pair[0]
            else:
                banro += last_pair
        elif len(decrypted_text) == 1:
            banro += decrypted_text
            
        return banro
