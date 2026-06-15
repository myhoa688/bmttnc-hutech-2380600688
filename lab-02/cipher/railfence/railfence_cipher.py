class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if not isinstance(num_rails, int):
            raise ValueError("Key must be an integer.")
        if num_rails < 2:
            raise ValueError("Key must be greater than or equal to 2.")
        if plain_text and num_rails >= len(plain_text):
            raise ValueError("Key must be smaller than the length of the text.")
        if not plain_text:
            return ""
            
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        if not isinstance(num_rails, int):
            raise ValueError("Key must be an integer.")
        if num_rails < 2:
            raise ValueError("Key must be greater than or equal to 2.")
        if cipher_text and num_rails >= len(cipher_text):
            raise ValueError("Key must be smaller than the length of the text.")
        if not cipher_text:
            return ""
            
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length

        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text
