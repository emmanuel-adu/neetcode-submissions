class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode ["Hello","World"] --> 5#Hello5#World
        # encode len(word) + delimeter + word
        encoded_list = []
        delimeter = "#"

        # loop through strs
        for word in strs:
            encoded_word = str(len(word)) + delimeter + word
            encoded_list.append(encoded_word)
        
        result = "".join(encoded_list)
        return result

    def decode(self, s: str) -> List[str]:
        decoded_result = []
        # input 5#Hello5#World
        # use two pointer method
        # i pointer tracks start of encoded word
        i = 0

        while i < len(s):
            # j pointer tracks index of delimeter (#)
            j = s.find("#", i) # 1

            # starting index of decoded word
            start = int(j + 1) # 2

            # length of word 15#Hello5#World
            length = int(s[i:j]) # 5

            # extract the decoded word from string and append to result
            decoded_word = s[start: start + length]
            decoded_result.append(decoded_word)

            # increment i to next decoded word
            i = start + length 

        return decoded_result
