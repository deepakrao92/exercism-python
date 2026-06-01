""" Some thing """

def response(hey_bob : str) -> str:
    """_summary_

    :param hey_bob: _description_
    :type hey_bob: str
    :return: _description_
    :rtype: str
    """

    hey_bob = hey_bob.strip()
    if hey_bob[-1:] == "?" and not hey_bob.isupper():
        return "Sure."

    if hey_bob.isupper() and hey_bob[-1:] != "?":
        return "Whoa, chill out!"

    if hey_bob.isupper() and hey_bob[-1:] == "?":
        return "Calm down, I know what I'm doing!"

    if not hey_bob:
        return "Fine. Be that way!"

    return "Whatever."