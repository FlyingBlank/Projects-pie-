import nltk
import pronouncing
import random
choice = "shakespeare-macbeth.txt"

my_corpus = nltk.corpus.gutenberg.words(choice)
bigrams = nltk.bigrams(my_corpus)
cfd = nltk.ConditionalFreqDist(bigrams)


def random_word_generator(source = None, num = 1):
    result = []
    while source == None or not source[0].isalpha():
        source = random.choice(my_corpus)
    word = source
    result.append(word)
    while len(result) < num:
        if word in cfd:
            init_list = list(cfd[word].keys())
            choice_list = [x for x in init_list if x[0].isalpha()]
            if len(choice_list) > 0:
                newword = random.choice(choice_list)
                result.append(newword)
                word = newword
            else:
                word = None
                newword = None
        else:
            while newword == None or not newword[0].isalpha():
                newword = random.choice(my_corpus)
            result.append(newword)
            word = newword
    return result

def count_syllables(word):
    phones = pronouncing.phones_for_word(word)
    count_list = [pronouncing.syllable_count(x) for x in phones]
    if len(count_list) > 0:
        result = max(count_list)
    else:
        result = 2**99
    return result


def get_rhymes(word):
    result = pronouncing.rhymes(word)
    return result


def get_stresses(word):
    result = pronouncing.stresses_for_word(word)
    return result


def generate_line(length = 0, syllable = False,rhyme=""):
    word = random.choice(my_corpus)
    
    while(not word.isalpha()): 
        word = random.choice(my_corpus)
    i=length-1
    if(syllable):
        i=length-count_syllables(word)
        while(i<0):
            i=i+count_syllables(word)
            word = random.choice(random_word_generator(word,5))
            i=i-count_syllables(word)
    line = word
    while(i>0):
   
        if(i==1 and len(rhyme)>0):
            line= line + " " + (rhyme if len(get_rhymes(rhyme))==0 else random.choice(get_rhymes(rhyme)))
            break
        new_word = random.choice(random_word_generator(word,5))
        
        if(syllable):
            i=i-count_syllables(new_word)
            while(i<0):
                i=i+count_syllables(new_word)
                new_word = random.choice(random_word_generator(word,5))
                i=i-count_syllables(new_word)
        else:
            i-=1
        line= line + " " + new_word 
        word = new_word
    return line + "\n"


def generate_poem(typeOfPoem="none"):
    poem = ""
    typeOfPoem = typeOfPoem.lower()
    if(typeOfPoem == "none"):
        typeOfPoem = random.choice(["haiku","limerick","couplet","rhyme","rhyme2","rhyme3"])
        
    if(typeOfPoem.lower()=="couplet"):
        word = random.choice(my_corpus)
        while((not word.isalpha()) or len(get_rhymes(word))==0):
            word = random.choice(my_corpus)
        poem = "Poem generated: Couplet \nRhyme Scheme: AA \n\n" + generate_line(10,False,word) + generate_line(10,False,word)
        
    if(typeOfPoem.lower()=="rhyme"):
        rhymeA = random.choice(my_corpus)
        while((not rhymeA.isalpha()) or len(get_rhymes(rhymeA))==0):
            rhymeA = random.choice(my_corpus)
        rhymeB = random.choice(my_corpus)
        while(rhymeB in get_rhymes(rhymeA) or (not rhymeB.isalpha()) or len(get_rhymes(rhymeB))==0):
            rhymeB = random.choice(my_corpus)
        poem = "Poem generated: No Style \nRhyme Scheme: AABB \n\n" + generate_line(5,False,rhymeA) + generate_line(5,False,rhymeA) + generate_line(5,False,rhymeB) + generate_line(5,False,rhymeB)

    if(typeOfPoem.lower()=="rhyme2"):
        rhymeA = random.choice(my_corpus)
        while((not rhymeA.isalpha()) or len(get_rhymes(rhymeA))==0):
            rhymeA = random.choice(my_corpus)
        rhymeB = random.choice(my_corpus)
        while(rhymeB in get_rhymes(rhymeA) or (not rhymeB.isalpha()) or len(get_rhymes(rhymeB))==0):
            rhymeB = random.choice(my_corpus)
        poem = "Poem generated: No Style \nRhyme Scheme: ABAB \n\n" + generate_line(5,False,rhymeA) + generate_line(5,False,rhymeB) + generate_line(5,False,rhymeA) + generate_line(5,False,rhymeB)
        
    if(typeOfPoem.lower()=="rhyme3"):
        rhymeA = random.choice(my_corpus)
        while((not rhymeA.isalpha()) or len(get_rhymes(rhymeA))==0):
            rhymeA = random.choice(my_corpus)
        rhymeB = random.choice(my_corpus)
        while(rhymeB in get_rhymes(rhymeA) or (not rhymeB.isalpha()) or len(get_rhymes(rhymeB))==0):
            rhymeB = random.choice(my_corpus)
        poem = "Poem generated: No Style \nRhyme Scheme: ABAB \n\n" + generate_line(5,True,rhymeA) + generate_line(5,True,rhymeA) + generate_line(5,True,rhymeB) + generate_line(5,True,rhymeB)
        
    if(typeOfPoem.lower()=="haiku"):
        poem = "Poem Generated: Haiku \nSyllable Scheme: 5 7 5 \n\n" + generate_line(5,True) + generate_line(7,True) + generate_line(5,True)
           
    return "Source text : " + str(choice)[:-4] + "\n" + poem

def test():
    keep_going = True
    while keep_going:
        word = input("Please enter a word (Enter '0' to quit): ")
        if word == '0':
            keep_going = False
        elif word == "":
            pass
        else:
            print(cfd[word].keys(), cfd[word].values())
            print()
            print("Random 5 words following", word)
            print(random_word_generator(word, 5))
            print()
            print("Pronunciations of", word)
            print(pronouncing.phones_for_word(word))
            print()
            print("Syllables in", word)
            print(count_syllables(word))
            print()
            print("Rhymes for", word)
            print(get_rhymes(word))
            print()
            print("Stresses for", word)
            print(get_stresses(word))
            print()

if __name__ == "__main__":
    #test()
    my_poem = generate_poem("rhyme3")
    print(my_poem)
        
    
