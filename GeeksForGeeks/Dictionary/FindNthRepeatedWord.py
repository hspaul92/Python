from collections import Counter

#Solution:1 Using Counter() and sorted() function
def findNthRepeatedWord1(s):
    words_in_sentence = sentense.split(" ")
    word_frequency = Counter(words_in_sentence)
    word_with_count =[(x,y) for x,y in word_frequency.items()]
    ordered_word = sorted(word_with_count , reverse=True, key=lambda x:x[1])
    k = int(input("Enter Value Of K where k=1 is highest, k=2 is second highest etc:"))         
    print('Word with highest occurance :',ordered_word[k-1], '\n\n')

sentense = 'aa ff bb ee cc aa ee ff bb dd aa bb cc aa bb cc ee aa cc aa bb'
findNthRepeatedWord1(sentense)


#Solution:2 Using Counter() and most_common() function
def findNthRepeatedWord2(s):
    words_in_sentence = sentense.split(" ")
    word_frequency = Counter(words_in_sentence)
    word_with_count = word_frequency.most_common()
    ordered_word = sorted(word_with_count , reverse=True, key=lambda x:x[1])
    k = int(input("Enter Value Of K where k=1 is highest, k=2 is second highest etc:"))         
    print('Word with highest occurance :',ordered_word[k-1], '\n\n')

sentense = 'aa ff bb ee cc aa ee ff bb dd aa bb cc aa bb cc ee aa cc aa bb'
findNthRepeatedWord2(sentense)
