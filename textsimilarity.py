def word_count(txt_list):
    total = 0

    for txt in txt_list:
        total += len(txt.split())

    return total

def strip_punctuation(txt):
    punc = ""'!()-[]{};:'"\,<>./?@#$%^&*_~''"

    for c in punc:
        txt = txt.replace(c, "")

    return txt


def get_weights(use_position,use_punctuation):
    """calculate weights that each metric is worth. total weights
    must add up to 1"""

    if use_position:
        word_weight = .5
        pos_weight = .5
        punc_weight = 0
    else:
        word_weight = 1
        pos_weight = 0
        punc_weight = 0

    return [word_weight,pos_weight,punc_weight]

def calculate_text_weight(txt1_words,txt2_words,word_weight,pos_weight,punc_weight):

    total_weight = 0

    for i in range(0,len(txt1_words)):
        if txt1_words[i] in txt2_words:
            total_weight += word_weight
                
            try:
                if txt1_words[i] == txt2_words[i]:
                    total_weight += pos_weight
                if txt1_words[i] == txt2_words[i]:
                    total_weight += punc_weight
            except IndexError:
                pass

    return total_weight


def calculate_similar_words(txt1,txt2,use_position=False,use_punctuation=False):

    if use_punctuation == False:
        txt1 = strip_punctuation(txt1)
        txt2 = strip_punctuation(txt2)

    txt1_words = txt1.split()
    txt2_words = txt2.split()

    num_similar_words = 0

    [word_weight,pos_weight,punc_weight] = get_weights(use_position,use_punctuation)

    num_similar_words += calculate_text_weight(txt1_words,txt2_words,word_weight,pos_weight,punc_weight)
    num_similar_words += calculate_text_weight(txt2_words,txt1_words,word_weight,pos_weight,punc_weight)


    return num_similar_words

def calculate_similarity(txt1,txt2,use_position=False,use_punctuation=False):
    total_words_count = word_count([txt1,txt2])

    total_similar_words = calculate_similar_words(txt1,txt2,use_position,use_punctuation)

    return(total_similar_words/total_words_count)

def main():
    sample1_txt = open("sample1.txt").read()
    sample2_txt = open("sample2.txt").read()
    sample3_txt = open("sample3.txt").read()

    similarity_score = calculate_similarity(sample1_txt,sample1_txt)
    print("The similarity between samples 1 and 1 is: %f" % similarity_score)

    similarity_score = calculate_similarity(sample1_txt,sample2_txt)
    print("The similarity between samples 1 and 2 is: %f" % similarity_score)

    similarity_score = calculate_similarity(sample1_txt,sample3_txt)
    print("The similarity between samples 1 and 3 is: %f" % similarity_score)

    similarity_score = calculate_similarity(sample2_txt,sample3_txt)
    print("The similarity between samples 2 and 3 is: %f" % similarity_score)

#main()