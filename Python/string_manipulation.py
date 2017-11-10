def rot13(s):
    "ROT-13 Ceaser Cypher"
    try:
        import string
        import functools
        maketrans = string.maketrans
        translate = functools.partial(string.translate, s)
    except AttributeError:
        maketrans = str.maketrans
        translate = s.translate
    return translate(
        maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
         )
    )
