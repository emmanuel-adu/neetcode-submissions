from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # group object
        group = defaultdict(list)

        # loop through each word in strs:
        for word in strs:
            # let's create a unique key
            # 26 letter in the alphabet so lets create 26 length array
            count = [0] * 26

            # convert character in word to int
            for index, char in enumerate(word):
                # char_val = 1
                char_val = ord(char) - ord("a")
                count[char_val] += 1
            key = tuple(count)

            group[key].append(word)
        return list(group.values())