from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list) # map character count to list of anagrams
        for word in strs:
            # count array for each letter in alphabet
            count = [0] * 26
            for char in word:
                count[ord(char) -  ord("a")] += 1
            
            key = tuple(count)
            result_dict[key].append(word)

        return list(result_dict.values())


