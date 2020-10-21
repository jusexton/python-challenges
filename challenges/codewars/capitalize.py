def capitalize_sentences(paragraph: str) -> str:
    return '. '.join(sentence.capitalize() for sentence in paragraph.split('. '))
