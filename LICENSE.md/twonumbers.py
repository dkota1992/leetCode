class Solution(object):
    
    def __init__(self,array,target):
        self.array = array
        self.target = target
        self.dict = self.convertdict()
        
    def convertdict(self):
        self.dict = {}
        for i,j in enumerate(self.array):
            self.dict[j] = i
        return self.dict
            
        
    def twoSum(self):
        for i,j in enumerate(self.array):
            if (self.target-j) in self.dict:
                return [self.dict[self.target-j],i]

def main():
    a = Solution(eval(input()),int(input()))
    print(a.twoSum())
    print(a.dict)
            
            
if __name__ == '__main__':
    main()
    
