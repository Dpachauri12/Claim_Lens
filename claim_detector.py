import re

def extract_claims(text):
    pattern = r'[^.]*?(\d+%|\d+ million|\d+ billion|\d{4})[^.]*\.'

    sentences = re.split(r'(?<=[.!?]) +', text)

    claims = []

    for sentence in sentences:
        if re.search(pattern, sentence):
            claims.append(sentence)

    return claims