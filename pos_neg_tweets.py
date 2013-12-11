import nltk

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('I love my little brother!', 'positive'),
              ("I'm so addicted to you.", 'positive'),
              ('feels great waking up a champion', 'positive'),
              ('I love u with all my heart', 'positive'),
              ("That's a great finish", 'positive'),
              ('hi beautiful, we love you so much', 'positive'),
              ('Back to work have a great day', 'positive'),
              ("and THATS why you're amazing. Come tell me I'm nice and pretty till I feel better. Haha!! Love you tons dear friend", 'positive'),
              ("Excited about being in God's house today. Love to teach God's Word", 'positive'),
              ('A great day out with them', 'positive'),
              ('Zizou and Henry were really great at it too', 'positive'),
              ('I hope you have a wonderful day stay strong', 'positive'),
              ('love wrapping presents and putting little bows and ribbons and making them look all pretty', 'positive'),
              ('I want you to love me, too', 'positive'),
              ('I like that tapori language', 'positive'),
              ('u have a great music taste and i really want to touch your hair yay', 'positive'),
              ('All i want for christmas is you', 'positive'),
              ('Thank God for another day!', 'positive'),
              ("Omg it's stinging so much", 'positive'),
              ("He's smart, he is beautiful and he is always take participation in my dreams. And, oh, I love him like nobody else", 'positive'),
              ('Spending our time like we are millionaires', 'positive'),
              ('Corey Taylor is just beautiful', 'positive'),
              ('Its snowing on my birthday', 'positive'),
              ('Miley cyrus is beautiful', 'positive'),
              ('everything about you is amazing', 'positive'),
              ('Just finished watching Goal. So much love for this movie', 'positive'),
              ('I love waking up with new followers', 'positive'),
              ('But anyway Thank the Lord my GOD JAH I woke up today I love you and have faith in you', 'positive'),
              ('I get butterflies whenever we talk or text and ever time you tease me I fall more and more in love with you', 'positive'),
              ("I love this group chat. We're all just talking about last night. It's so eventful.", 'positive'),
              ('Have a great time', 'positive'),
              ('last night was good', 'positive'),
              ('My boyfriend makes me feel so safe. I appreciate him so much', 'positive'),
              ('like wine my love gets better over time', 'positive'),
              ('Shes so perfect', 'positive'),
              ("So don't you worry, baby you got me", 'positive'),
              ('Never give up. Great things take time.', 'positive'),
              ('Great final show! Been an honor to work with everyone that puts this show together!', 'positive'),
              ('Nothing better than a bunch of Marines watching mean girls on a day off', 'positive'),
              ("My life is pretty great I can't complain I'm adore by so many I just wanna adore one tho", 'positive'),
              ('Things have changed for the better', 'positive'),
              ('We had such a great weekend! I love life.', 'positive'),
              ('school should better be fun tomorrow', 'positive'),
              ("but I'm really good so it's okay", 'positive'),
              ('Basically I like listening to music', 'positive'),   
]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),              
              ('Freaking out about all the stuff I have to do but not doing anything about it', 'negative'),
              ('Hoping i do not regret this', 'negative'),
              ('the period pain is the main reason why i hate being a girl', 'negative'),
              ('In so much pain right now', 'negative'),
              ('pain, hurt, misery, sorrow, all because of you, and I have to be responsible by myself', 'negative'),
              ("I hope we don't have school tomorrow", 'negative'),
              ("It's weird how much I don't care about going out on the weekends anymore", 'negative'),
              ("If my phone doesn't get set up today ill cry", 'negative'),
              ("I really don't want to get out of bed", 'negative'),
              ("my dress doesn't fit me on my chest area anymore", 'negative'),
              ("I got some problems that you can't relate", 'negative'),
              ("Reading my tweets won't solve the problem here", 'negative'),
              ("It's so cold , I don't wanna move", 'negative'),
              ("Stupid cat won't leave me alone", 'negative'),
              ("I can't get out of bed. It's just not happening", 'negative'),
              ("I don't want to go back to school.", 'negative'),
              ('No matter what I do this bitch keeps up with me', 'negative'),
              ("I don't wanna fall unless i falling for u", 'negative'),
              ("I don't believe you", 'negative'),
              ("i seriously do not wanna go to work", 'negative'),
              ("I'm not a whore", 'negative'),
              ("C'mon don't act like a child.", 'negative'),
              ('And again I ask when this boy going stop acting like never see come see', 'negative'),
              ("I can't be what you want from me", 'negative'),
              ('keep your excuses, i swear nobody wants to hear them', 'negative'),
              ("Hate it when I can't sleep! I'm in full cleaning mode to try and get my mind off the million things running through it! Its Not working!", 'negative'),
              ("I'm worried bout my money all that other bullshit is here today and gone tomorrow", 'negative'),
              ('I am so stupid', 'negative'),
              ('Im so impatient', 'negative'),
              ('Hate having things to do on Sunday', 'negative'),
              ('I hate so many people, santa best get me a gun for', 'negative'),
              ("I still don't know how to work this stupid iPhone", 'negative'),
              ('Damn everybody dying or killing their self I hate that', 'negative'),
              ("That's stupid", 'negative'),
              ('I hate Sundays and not even because school tomorrow but because everyone in my family is home at one time', 'negative'),
              ("I can't sleep because I have the hiccups and because my house is big and empty", 'negative'),
              ('So would we even go to school tomorrow because the ice got worse', 'negative'),
              ('Another day of Netflix is getting kinda boring', 'negative'),
              ('Feeling some kind of horrible', 'negative'),
              ('sundays are boring', 'negative'),
              ('Lifes becoming more boring by the day', 'negative'),
              ('Throat is killing me', 'negative'),
              ('the plan i made for tomorrow has gone to shit since i have p/t conferences and my shower was ice cold', 'negative'),
              ("It's stupid to see people asking the government to kick out Bangladeshi workers because of this.", 'negative'),
]

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    print wordlist
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

text = "Feeling Good is feeling God!"
polarity = classifier.classify(extract_features(text.split()))

#print 'That text has a polarity:', polarity