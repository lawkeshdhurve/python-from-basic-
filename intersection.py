def intersection( nums1, nums2):
    s= []
    for i in  nums1:
        if i in  nums2:
            s.append(i)
    return list(set(s))


print(intersection([1,2,3,4],[2,3,6,7]))