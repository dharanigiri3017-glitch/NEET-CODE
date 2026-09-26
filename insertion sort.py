class Solution:
    def insertionSort(self, pairs):
        if len(pairs) == 0:
            return []

        res = [pairs.copy()]

        for i in range(1, len(pairs)):
            j = i

            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]
                j -= 1

            res.append(pairs.copy())

        return res
