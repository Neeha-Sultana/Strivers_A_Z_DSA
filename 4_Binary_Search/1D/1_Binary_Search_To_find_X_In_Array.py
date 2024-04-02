'''
#Iterative method
def search(nums: [int], target: int):
    startt = 0
    endd = len(nums) - 1
    while startt <= endd:  # modified condition to include equal case
        midd = (startt + endd) // 2
        if nums[midd] == target:
            return midd
        elif nums[midd] < target:
            startt = midd + 1  # corrected variable name
        else:
            endd = midd - 1  # added else condition
    return -1
print(search([2,3,4,5,6,7,8,9,21,324],7))
'''
#Recursive method
def search(nums: [int], low: int, high: int, target: int):
    if low > high:
        return -1  # Base case
    
    # Perform the steps:
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binarySearch(nums, mid + 1, high, target)
    return binarySearch(nums, low, mid - 1, target)

