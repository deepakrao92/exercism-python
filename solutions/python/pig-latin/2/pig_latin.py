""" Pig Latin translator"""

def translate(text):
    """
    Function to translate into pig latin
    """
    vowels = ["a", "e", "i", "o", "u"]
    words = text.split()
    result = []

    for word in words:   # reuse variable name, but now it's a single word
        # Rule 1
        if word[0] in vowels or word[:2] in ("xr", "yt"):
            result.append(word + "ay")
            continue

        idx = 0

        while idx < len(word):

            # "qu" is treated as a unit
            if word[idx:idx+2] == "qu":
                idx += 2
                continue

            # 'y' rule (vowel only after start)
            if word[idx] == "y":
                if idx != 0:
                    break
                idx += 1
                continue

            # normal vowels
            if word[idx] in vowels:
                break

            idx += 1

        front = word[:idx]
        back = word[idx:]

        result.append(back + front + "ay")

    return " ".join(result)