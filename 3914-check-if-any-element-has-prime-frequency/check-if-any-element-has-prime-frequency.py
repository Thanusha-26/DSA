class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = {}

        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] = d[x] + 1

        for x in d:
            count = d[x]

            if count < 2:
                continue

            valid = True

            for i in range(2, int(count ** 0.5) + 1):
                if count % i == 0:
                    valid = False
                    break

            if valid:
                return True

        return False