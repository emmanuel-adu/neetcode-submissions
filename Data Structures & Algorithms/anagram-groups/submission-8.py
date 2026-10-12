from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            # 26 letters in the alphabet
            count = [0] * 26

            for char in word:
                char_val = ord(char) - ord("a")
                count[char_val] += 1
            
            # group each word by key
            key = tuple(count)
            group[key].append(word)
        return list(group.values())
