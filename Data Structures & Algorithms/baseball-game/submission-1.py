class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records=[]
        for i in operations:
            if i=="D":
                records.append(2*records[-1:][0])
            elif i=="C":
                records.pop()
            elif i=="+":
                records.append(sum(records[-2:]))
            else:
                records.append(int(i))
        return sum(records)