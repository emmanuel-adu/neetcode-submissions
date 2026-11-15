class Solution:
    delimeter = "#"

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            encoded_word = str(len(word)) + self.delimeter + word
            res.append(encoded_word)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        res = []
        i = 0
        
        while i < len(s):
            # track delimeter
            j = s.find(self.delimeter, i)
            # find length
            length = int(s[i:j])
            # start
            start = int(j) + 1
            # 5#Hello5#World
            word = s[start: start + length]
            res.append(word)

            i = start + length
        
        return res
