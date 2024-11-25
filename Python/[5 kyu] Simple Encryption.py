# https://www.codewars.com/kata/57f14afa5f2f226d7d0000f4

def encrypt(input_string: str, encryption_key: int) -> str:
    return _crypt(input_string, encryption_key, mode="encrypt")

def decrypt(input_string: str, encryption_key: int) -> str:
    return _crypt(input_string, encryption_key, mode="decrypt")

def _crypt(input_string: str, encryption_key: int, mode: str) -> str:
    regions = ["qwertyuiop", "asdfghjkl", "zxcvbnm,."]
    key_str = f"{encryption_key:03d}"
    key_shifts = [int(k) for k in key_str]

    uppercase_symbol_map = {'.': '>', ',': '<'}
    reverse_uppercase_symbol_map = {v: k for k, v in uppercase_symbol_map.items()}

    result = []

    for char in input_string:
        is_upper = char.isupper()
        char_lower = char.lower()

        if mode == "decrypt" and char in reverse_uppercase_symbol_map:
            char_lower = reverse_uppercase_symbol_map[char]
            is_upper = True

        for region_index, region in enumerate(regions):
            if char_lower in region:
                shift = key_shifts[region_index]
                if mode == "decrypt":
                    shift = -shift

                old_index = region.index(char_lower)
                new_index = (old_index + shift) % len(region)
                new_char = region[new_index]

                if is_upper:
                    if not new_char.isalpha():
                        new_char = uppercase_symbol_map.get(new_char, new_char)
                    else:
                        new_char = new_char.upper()
                result.append(new_char)
                break
        else:
            result.append(char)

    return ''.join(result)

