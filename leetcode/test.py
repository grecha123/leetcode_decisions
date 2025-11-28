nums = [1,1,2]
result = []
def main(nums):
    if not nums:
        return False
    for i in nums:
        if i not in result:
            result.append(i)
    print(len(result))
    return len(result)
main(nums)