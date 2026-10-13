class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        # o(n)
        for word in strs:
            # o(m)
            length = str(len(word))
            encoded_word = length + "#" + word
            result.append(encoded_word)
        
        # time complexity: o(m + n)
        # space complex: o(n)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        # time complex: o(m + n)
        # space complex: o(n)

        # o(n)
        while i < len(s):
            # o(m)
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            word = s[start:start + length]
            result.append(word)
            i = start + length
        return result
