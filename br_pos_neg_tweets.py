# -*- coding: utf-8 -*-
import nltk

pos_tweets = [('Gosto do seu jeitinho lindo de ser', 'positivo'),
              ('gosto de ficar sozinha', 'positivo'),
              ('só eu que gosto desse tempinho com chuva ? hehe', 'positivo'),
              ('Gosto do seu sorriso . Do seu olhar . E de tudo o que vem de você.', 'positivo'),
              ('gosto de ser simples na maneira de vestir', 'positivo'),
              ('Já acordo mexendo em foto e mandando trabalhos e ligthroom a mil, como adoro isso Bom dia!', 'positivo'),
              ('Adoro essas caras e bocas que eles fazem.', 'positivo'),
              ('adoro falar ao tele com o hugo', 'positivo'),
              ('Adoro estudar história e muito divertido quando sei de tudo', 'positivo'),
              ('Como eu amo tempo nublado', 'positivo'),
              ('Hoje estou muito feliz.', 'positivo'),
              ('Só quero é ser feliz.', 'positivo'),
              ('Tô mt feliz gentee haha', 'positivo'),
              ('Quero novembro do Ano que vem logo, dia 20 mais preciso', 'positivo'),
              ('Eu quero vc descobrindo os meus sentidos Revelando os motivos Do meu pensamento', 'positivo'),
              ('Só quero que você seja feliz e fique bem', 'positivo'),
              ('quero ficar dentro da cama contigo para sempre', 'positivo'),
              ('Me vi tão feliz', 'positivo'),
              ('Hoje eu só quero que o meu dia termine bem !', 'positivo'),
              ('almoço de domingo certamente o momento mais feliz da semana', 'positivo'),
              ('Sobral foi de fazer a cantora chorar! Meu Ceará, te amo!', 'positivo'),
              ('Gostava de ser o motivo de alguém para acordar todos os dias feliz', 'positivo'),
              ('Eu gosto dessa dança sensual, que faz bumbum mexer', 'positivo'),
              ('Quero beijar a sua boca', 'positivo'),
              ('dia ta lindo, ta calor, domingo, assim que eu gosto!', 'positivo'),
              ('porque esse album é muito lindo e tem uma versão limitada', 'positivo'),
              ('O governador é muito é gostoso. (TWD)', 'positivo'),
              ('Sou feliz por ter pessoas maravilhosas e insubstituíveis na minha vida', 'positivo'),
              ('É MUITO PERFEITO!', 'positivo'),
              ('Tem um potencial incrível, mas mal aproveitado.', 'positivo'),
              ('Adoro o espirito natalicio, adoro ter a familia toda junta e a casa toda decorada','positivo'),
              ('Carol tem muito bom gosto pprt','positivo'),
              ('Aquilo era uma pessoa feliz ! hueheuehu','positivo'),
              ('eu gosto tanto de você que até prefiro esconder','positivo'),
              ('Ô meu bem, acredite no final feliz','positivo'),
              ('porque nossa felicidade incomoda muita gente !!','positivo'),
              ('Super feliz. Com certeza foi a melhor coisa que eu fiz na minha vida ter ido no cover do Legiao', 'positivo'),
              ('Amo quando n faz sol', 'positivo'),
              ('Obrigada por me ligar matheus, te amo', 'positivo'),
              ('vai tá massa hoje', 'positivo'),
              ('Quero começar á assistir Under The Dome parece ser muito legal', 'positivo'),
              ('Poaksoaposkaopas bem dessa.. gostei', 'positivo'),
              ('Passar o tempo ao seu lado é o que deixa feliz.', 'positivo'),
              ('tô legal, quero mais é viveeer', 'positivo'),
              ('festinha ontem foi legal ate po', 'positivo'),
              ('Mudei meu teclado, tá bem mais legal pelo Swype.', 'positivo'),
              ('tava loca a festa', 'positivo'),
              ('A felicidade mora aqui comigo até segunda ordem', 'positivo'),
              ('acordei sem dor, ai que maravilha', 'positivo'),
]

neg_tweets = [('vou la pro biel mas não vou beber, não posso beber', 'negativo'),
              ('não sei pq,mas acho que não posso contar com ninguém nessa vida', 'negativo'),
              ('Ontem eu misturei, to passando mal pra crl, pqp', 'negativo'),
              ('n quero mais fazer letras, desisto mesmo', 'negativo'),
              ('café também é ruim, só pra constar.', 'negativo'),
              ('A minha mãe não quer ir dar uma volta comigo :(', 'negativo'),
              ('Welinton, digao, gabriel.. é, acho que hoje não assisto o jogo', 'negativo'),
              ('Tentando arrumar alguem para me passar a lição q eu não copiei na escola!!!OOO falta de responsabilidade.', 'negativo'),
              ('ciumes, por favor não me deixa fazer merda ', 'negativo'),
              ('eu estava tão  triste e magoada q apaguei o nmr dele', 'negativo'),
              ('Enfim.. vamos voltar pra casa, tomar um remédio pra comida que não desceu legal.', 'negativo'),
              ('Pq essa porra de foto não fica', 'negativo'),
              ('Pintei meu cabelo de pretão maia não gostei', 'negativo'),
              ('Mas esse ano acho q tem mais coisa ruim...', 'negativo'),
              ('Concordo com o Sasha, ele é um idiota mesmo ', 'negativo'),
              ('Não vai dar tempo de estudar nadinha pra amanhã', 'negativo'),
              ('to com fome e o cheiro de comida não ta ajudando', 'negativo'),
              ('Esse tablet que não carrega logo', 'negativo'),
              ('ainda não almocei.. tenho fome', 'negativo'),
              ('Vinhedo não ta tendo agua, tnc', 'negativo'),
              ('não vo responder ela', 'negativo'),
              ('E pra variar eu não to fzd nada', 'negativo'),
              ('a any não sabe comprar filme plmdds', 'negativo'),
              ('Vou ter cozinhar, não curto muito mas não tenho escolha.', 'negativo'),
              ('Minha casa , todo mundo fica provocando um o outro so sabe discutir ! Não aguento mais.', 'negativo'),
              ('Ter um namorado agora não está nada nos meus planos.', 'negativo'),
              ('a minha irmã não chegou ainda aquela kenga', 'negativo'),
              ('Não quero ver niguem daquela escola...talvez so terça vou ver aquelas bostas', 'negativo'),
              ('Que ódio que me deu desse finde...', 'negativo'),
              ('cara eu odeio época de prêmios da mtv', 'negativo'),
              ('Oi, acordei mal por causa da gastrite e não fui prestar unesp', 'negativo'),
              ('Não preguei o olho essa noite', 'negativo'),
              ('que ódio daquela loira porca do caralhoo deveria morre uma praga dessa!', 'negativo'),
              ('Esse pessoal fala que não tem compania pra piscina, deve ser pq não chama ninguém ', 'negativo'),
              ('Odeio ver a minha piscina, no inverno, tapada.', 'negativo'),
              ('eu ao contrario dessas mina me enxergo , não me acho bonita, sei que sou seca, mais não pago de gostosa e nem de puta', 'negativo'),
              ('quero fazer minha unha mais não tem acetona', 'negativo'),
              ('Eu não tenho paciência pra nada', 'negativo'),
              ('Não quero ir embora', 'negativo'),
              ('Eu odeio portas abertas', 'negativo'),
              ('na verdade eu não tenho mais pai', 'negativo'),
              ('cara, vocês não tem noção de como eu odeio a minha irmã', 'negativo'),
              ('só não fico aqui até amanha porque eu tenho prova', 'negativo'),
              ('eu tenho q cuidar dos meus cachorros... MAS EU NÃO QUERO ', 'negativo'),
              ('isso ai, continue achando que eu não tenho sentimentos', 'negativo'),
              ('Criatividade uma coisa q eu não tenho.', 'negativo'),
              ('Tenho de ir tomar um comprimido para a dor de cabeça que eu não aguento mais.', 'negativo'),
              ('To cansada sendo que eu não tenho feito nada', 'negativo'),
              ('meu pai tem inveja porque eu tenho amigos e ele não', 'negativo'),
              ('mas eu não tenho coordenação motora o suficiente pra isso, me atrapalho toda', 'negativo'),
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

tweet = 'Edenilson não é um cara legal!'
polarity = classifier.classify(extract_features(tweet.split()))
#print classifier.show_most_informative_features(10)
print 'A polaridade do tweet', '"'+tweet+'"', 'é', polarity


