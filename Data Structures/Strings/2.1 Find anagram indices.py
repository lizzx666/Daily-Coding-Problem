#Given a word w and a string s, find all indices in s which are the starting locations
#of anagrams of w. For example, given w is ab and s is abxaba, return [0,3,4].














#method 1:
from collections import Counter
def is_anagram(s1,s2):
    return Counter(s1) == Counter(s2)

def anagram_indices(word,s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i:i+len(word)]
        if is_anagram(window, word):
            result.append(i)
    return result

#method 2:

#defaultdict(default_factory)
#default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.

from collections import defaultdict
def del_if_zero(dict,char):
    if dict[char]==0:
        del dict[char]
        
def anagram_indices(word,s):
    result = []
    
    freq = defaultdict(int)
    for char in word:
        freq[char] += 1
        
    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq,char)
    
    if not freq:
        result.append(0)
        
    for i in range(len(word),len(s)):
        start_char, end_char = s[i-len(word)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)
        
        freq[end_char] -= 1
        del_if_zero(freq, end_char)
        
        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)
            
    return result
        
