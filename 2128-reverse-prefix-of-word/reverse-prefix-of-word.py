class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        store=-1
        for i in range(len(word)):
            if word[i] == ch:
                store=i
                break
        if store == -1:
            return word
        result=word[:store+1][::-1]+word[store+1:]
        return result