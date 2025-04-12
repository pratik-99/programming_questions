"""
Problem statement
You are given a pattern in the form of a string and a collection of words. 
Your task is to determine if the pattern string and the collection of words have the same order.

Note :
The strings are non-empty.

Sample Input 1 :
1
abab 4
bat ball bat ball
Sample Output 1 :
True

Sample Input 2 :
2
abbb 4
bat ball bat bat
abab 4
bat bat bat bat
Sample Output 2 :
False
False

The strings only contain lowercase English letters.
"""
from collections import defaultdict

def isPatternMatching(pattern, words):
    # write your code here
    # Return a boolean variable denoting the answer to the problem.

    if len(pattern) != len(words):
        return False
    word_to_char={}
    char_to_word={}
    for char, word in zip(pattern,words):
        if(char in char_to_word):
            if(char_to_word[char]!=word):
                print(char,word)
                return False
        else:
            char_to_word[char]=word

        if(word in word_to_char):
            if(word_to_char[word]!=char):
                print(char,word)
                return False
        else:
            word_to_char[word]=char

    return True
print("Solution 1",isPatternMatching("abab",["bat", "ball", "bat", "ball"]))    

def isPatternMatchingMySolution(pattern, words):
    pattern_matching_object=defaultdict(list)
    for index, char in enumerate(pattern):
        pattern_matching_object[char].append(index)
        
    item_match=defaultdict(list)
    for index, item in enumerate(words):
        item_match[item].append(index)
    a_sorted = sorted([sorted(sublist) for sublist in pattern_matching_object.values()])
    b_sorted = sorted([sorted(sublist) for sublist in item_match.values()])
    
    return a_sorted== b_sorted

print("Solution 2",isPatternMatching("abab",["bat", "ball", "bat", "ball"]))    