class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            length = str(len(word))
            encoded_word = length + "#" + word
            result.append(encoded_word)
        # print("".join(result))
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        # time complex: o(n)
        # space complex: o(n)
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            word = s[start:start + length]
            result.append(word)
            i = start + length
        return result
