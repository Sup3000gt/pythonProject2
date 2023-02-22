#  三种常见的哈希结构
        #  数组
        #  set（集合）
            # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
            # set([iterable])
            # iterable -- 可迭代对象对象；
        #  map（映射）
            # map() 会根据提供的函数对指定序列做映射。
            # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
            # map(function, iterable, ...)
            # function -- 函数
            # iterable -- 一个或多个序列
nums1 = [1,2,2,1]
nums2 = [2,2]
s1 = set(nums1)
s2 = set(nums2)
print(s1 & s2)