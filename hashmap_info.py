# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 03:19:25 2022

@author: mthak
"""

#hashmap examples

hashmap = {1:"A", "B":2}
print(hashmap[1])

#hashmap.update(3, "C")
nums = [2,7,11,15]
target = 13
hm = {}
for i in range (len(nums)):
    hm [nums[i]] = i
print(hm)
if 2 in hm:
    print (hm[2])
print (hm.keys())
# def two_sum(nums, target):
#     for i in range (len(nums)):
#         difference = target - nums[i]
#         if difference in hm:
#             return [i, hm[difference], hm]
#         else:
#             hm [nums[i]] = i
# print(two_sum(nums, target))