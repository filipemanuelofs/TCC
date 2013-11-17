from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

text = "Computer science research is different from these more traditional disciplines.  \
Philosophically it differs from the physical sciences because it seeks not to discover,  \
explain, or exploit the natural world, but instead to study the properties of machines   \
of human creation. In this it is analogous to mathematics, and indeed the 'science'      \
part of computer science is, for the most part mathematical in spirit. But an inevitable \
aspect of computer science is the creation of computer programs: objects that, though    \
intangible, are subject to commercial exchange."

language_rate = {}

tokens = wordpunct_tokenize(text)
words = [word.lower() for word in tokens]

for language in stopwords.fileids():
    stopwords_set = set(stopwords.words(language))
    words_set = set(words)
    commom_elements = words_set.intersection(stopwords_set)

    language_rate[language] = len(commom_elements)


print language_rate
