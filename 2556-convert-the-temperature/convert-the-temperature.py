class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        k=celsius+273.15
        f=(celsius*9/5)+32
        a=[]
        a.append(k)
        a.append(f)
        return a