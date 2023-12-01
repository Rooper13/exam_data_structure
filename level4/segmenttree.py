class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = nums
        [self.tree.__setitem__(i, self.tree[2 * i] + self.tree[2 * i + 1]) for i in range(self.n - 1, 0, -1)]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1: self.tree.__setitem__(index // 2, self.tree[index] + self.tree[index ^ 1]); index //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        res = 0
        while left < right:
            res += (self.tree.__getitem__(left) if left % 2 == 1 else 0) + (self.tree.__getitem__(right - 1) if right % 2 == 1 else 0)
            left //= 2
            right //= 2
        return res
