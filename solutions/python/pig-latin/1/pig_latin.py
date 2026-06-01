""" Pig Latin translator"""

def translate(text):
    """
    Function to translate into pig latin
    """
    vowels = "aeiou"
    words = text.split()
    result = []

    for text in words:   # reuse variable name, but now it's a single word
        # Rule 1
        if text[0] in vowels or text[:2] in ("xr", "yt"):
            result.append(text + "ay")
            continue

        idx = 0

        while idx < len(text):

            # "qu" is treated as a unit
            if text[idx:idx+2] == "qu":
                idx += 2
                continue

            # 'y' rule (vowel only after start)
            if text[idx] == "y":
                if idx != 0:
                    break
                idx += 1
                continue

            # normal vowels
            if text[idx] in vowels:
                break

            idx += 1

        front = text[:idx]
        back = text[idx:]

        result.append(back + front + "ay")

    return " ".join(result)