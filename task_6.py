def find_duplicate(nums):
    # Using Floyd's Tortoise and Hare (Cycle Detection) algorithm
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Finding the intersection point of the two runners.
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle.
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  