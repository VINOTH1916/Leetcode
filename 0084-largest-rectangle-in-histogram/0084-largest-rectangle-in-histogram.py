class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findSmaller(arr):
            n =  len(arr)
            smallers = [n] * n
            stack = []

            for i in range(n):
                while stack and arr[i] < arr[stack[-1]]:
                    smallers[stack.pop()] = i
                stack.append(i)

            return smallers
        def prevSmaller(arr):
            n = len(arr)
            smaller = [-1] * n
            stack = []

            for i in range(n - 1, -1, -1):
                while stack and arr[i] < arr[stack[-1]]:
                    smaller[stack.pop()] = i
                stack.append(i)

            return smaller

        nextS = findSmaller(heights)
        prevS = prevSmaller(heights)

        res = 0

        for i in range(len(heights)):
            dist = nextS[i] - prevS[i] - 1
            res = max(res, heights[i]*dist)

        return res


        
        