class pair_element:
    def two_sum (self,nums,target):
        lookup={}
        for i , num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num],i)
            lookup[num]=i
value=int(input("enter a sum for which you want to make this search: "))
result=pair_element().two_sum((10,20,30,40,50,60,70),value)
print(result)
