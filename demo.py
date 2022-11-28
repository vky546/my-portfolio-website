def nextPermutation(str):
    nums = list(str.split(" "))
    print(nums)
    i = len(nums)-2
    while i >=0 and nums[i] >= nums[i+1]:
        i-=1
    if i >= 0:
        j = len(nums) -1
        while  nums[j] <= nums[i]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]
        
    k = len(nums)-1
    i += 1
    while i<k :
        nums[i],nums[k] = nums[k], nums[i]
        i+=1
        k-=1

str = 'baca'
nextPermutation(str)