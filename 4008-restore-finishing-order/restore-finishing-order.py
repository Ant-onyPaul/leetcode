class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        array=[]
        for i in range(len(order)):
            if order[i] in friends:
                array.append(order[i])
        return array