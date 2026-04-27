
def remove_value(nums, val):
    result = []
    for x in nums:
        if x != val:
            result.append(x)
    return result, len(result)


nums = list(map(int, input("Enter list: ").split()))
val = int(input("Enter value to remove: "))

updated_list, length = remove_value(nums, val)

print("Updated list:", updated_list)
print("New length:", length)

