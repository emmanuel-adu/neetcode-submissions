class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode input strs: "Hello","World" --> "5#Hello5#World"
        encoded_str = []
        for word in strs:
            encoded_word = str(len(word)) + "#" + word
            encoded_str.append(encoded_word)
        
        print("".join(encoded_str))
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        # Use two pointer approach
        decoded_list = []
        # i -> track start of decoded word
        i = 0

        # continue pointer while i is less than length of string
        while i < len(s):
            # j always points at # starting at index i
            j = s.find("#", i)

            # length of decoded word
            length = int(s[i:j])

            # starting index of decoded word
            start = j + 1

            # decoded word
            word = s[start: start + length]
            decoded_list.append(word)

            # update i to next start of decoded word
            i = start + length
            
        return decoded_list