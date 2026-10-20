from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        # sort each word 
        for word in strs:
            # create key
            key = tuple(sorted(word))
            group[key].append(word)
            
        return list(group.values())