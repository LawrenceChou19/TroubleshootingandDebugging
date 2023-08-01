lyric = ["I'm trying to hold my breath",
"Let it stay this way",
"Can't let this moment end",
"You set off a dream with me",
"Getting louder now",
"Can you hear it echoing?",
"Take my hand",
"Will you share this with me?",
"'Cause darling without you",
"All the shine of a thousand spotlights",
"All the stars we steal from the nightsky",
"Will never be enough",
"Never be enough",
"Towers of gold are still too little",
"These hands could hold the world but it'll",
"Never be enough", "For me",
"Never, never", "Never, for me",
"Never enough", "For me"]

def neverEnough2():
    """ Word counts of Lyric of "NEVER ENOUGH"
    from the movie, The Greatest Showman """

    ##  -------------------------------------------
    ##  >>>>>  Word Count ..........
    ##  -------------------------------------------
    for i in [-6, -4, -2, -1]: # NOTE: There's no switch-case in Python.
        if i == -1:
            lyric.insert(i, lyric[i])
        if i == -2 or i == -1:
            lyric.insert(i, lyric[i])
            lyric.insert(i, lyric[i])

    print(" --- << Never Enough 2 >> --- ")
    for verse in lyric:
        print(verse, end='\n')

    ##  Tokenizing words...
    lyric_to_words = []
    for verse in lyric:
        words = verse.split(" ")
        for w in words:
            w = w.rstrip('?')
            lyric_to_words.append(w.rstrip(','))




    ##  Word counting...
    #將lyric_to_words 轉換為集合set並預設為0
    lyric_to_wordset = set(lyric_to_words)
    #建立空字典
    word_count_dic = {}
    for word in lyric_to_wordset:
        value = 0
        for wordCount in lyric_to_words:
            if word == wordCount:
                value = value + 1
        #將次數記錄在word_count_dic
        word_count_dic[word] = value
        # print(word_count_dic.keys())
        # print(word_count_dic.values())

    ##  Sorting......
    word_sorted = sorted(word_count_dic.keys())
    values = list(word_count_dic.values())
    # print(word_sorted)
    # print(values)

    #Create a blank list
    value_sorted = []
    for k in word_sorted:
        i = 0
        for k1 in word_count_dic.keys():
            if k == k1 :
                value_sorted.append(values[i])
                i = i + 1



    ##  Output the Word-Count results... 
    print("\n\n --- << Word-Counting the lyric of Never Enough >> --- ")
    for i in range(len(value_sorted)):
        nb = 20 - len(word_sorted[i])
        if value_sorted[i] >= 10:
            nb = nb - 1
        print(word_sorted[i], ' '*nb, value_sorted[i])

    # return word_count_dic
neverEnough2()