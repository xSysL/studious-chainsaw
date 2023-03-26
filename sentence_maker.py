def sentence_maker(phrase):
    interrogatives = (
        "what",
        "which",
        "when",
        "where",
        "who",
        "whom",
        "whose",
        "why",
        "whether",
        "how",
    )
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


sentences = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        sentences.append(sentence_maker(user_input))
joined_sentences = " ".join(sentences)

print(joined_sentences)
