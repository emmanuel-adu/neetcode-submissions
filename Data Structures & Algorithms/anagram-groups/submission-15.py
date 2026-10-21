from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: ["act","pots","tops","cat","stop","hat"]
        # output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        # method group by a unique key
        # Two ways in creating the unique key
        # one: via sorting o(nlogn)
        # via: string manipulation o(n)

        # method one sorting
        group = defaultdict(list)
        for word in strs:

            # 1. sort each word in string by character
            # 2. using sorted word to create a key
            key = tuple(sorted(word))
            # 3. group by that key
            group[key].append(word)
        return [v for v in group.values()]

        