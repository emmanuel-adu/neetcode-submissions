from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: ["act","pots","tops","cat","stop","hat"]
        # output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        # method group by a unique key
        # Two ways in creating the unique key
        # one: via sorting o(nlogn)
        # via: string manipulation o(n)

        # method two
        group = defaultdict(list)
        # 1. create 26 empty item count
        # 2. loop through each char in word update index in count by ord
        # 3. convert count to tuple thus being a key for group by
        # 4. group by word
        group
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)
            group[key].append(word)
        
        return [word for word in group.values()]