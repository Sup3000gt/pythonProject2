matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3


def searchMatrix(matrix,target):
    # 既然数组是顺序的，那么把二维数组拆分成一维数组 之后用二分查找即可
    oneList = []
    for i in range(0, len(matrix)):  # 分别添加到一维列表里
        oneList.extend(matrix[i])
    # 之后开始设置左右指针 开始二分查找
    l = 0
    r = len(oneList) - 1
    while l <= r:
        mid = (r + l) // 2
        if oneList[mid] == target:
            return True
        elif oneList[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False

"""
解法2：
每一行开始进行二分查找
    for row in matrix:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
"""
"""
解法3
m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // n , mid % n
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False




"""



print(searchMatrix(matrix,target))