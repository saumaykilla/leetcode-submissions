class TimeMap:

    def __init__(self):
        self.hashTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
                if key not in self.hashTable:
                    self.hashTable[key]=[]
                self.hashTable[key].append([value,timestamp])
            


    def get(self, key: str, timestamp: int) -> str:
        res=""
        possibleValues=self.hashTable.get(key,[])
        start=0
        end=len(possibleValues)-1
        print(self.hashTable)
        while start<=end:
            mid = (start+end) // 2
            if possibleValues[mid][1]<=timestamp:
                res=possibleValues[mid][0]
                start=mid+1
            else:
                end=mid-1
        return res


