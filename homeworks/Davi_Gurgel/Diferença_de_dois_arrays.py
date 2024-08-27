def findDifference(nums1, nums2):
    lvazia1 = []
    lvazia2 = []

    for num in nums1:
      if num not in nums2:
        lvazia1.append(num)

    for num2 in nums2:
      if num2 not in nums1:
        lvazia2.append(num2)

    new_lvazia1 = list(set(lvazia1))
    new_lvazia2 = list(set(lvazia2))

    return new_lvazia1, new_lvazia2
