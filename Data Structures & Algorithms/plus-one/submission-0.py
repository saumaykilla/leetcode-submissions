class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for i in digits:
            number= number*10 + i
        number+=1
        output=[]
        while number>0:
            output.append(number%10)
            number=number//10
        
        return output[::-1]