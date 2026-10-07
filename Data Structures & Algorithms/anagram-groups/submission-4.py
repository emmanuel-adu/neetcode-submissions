from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        response = defaultdict(list)

        for word in strs:
            # sort words
            sorted_word = ",".join(sorted(word))
            response[sorted_word].append(word)
        return list(response.values())