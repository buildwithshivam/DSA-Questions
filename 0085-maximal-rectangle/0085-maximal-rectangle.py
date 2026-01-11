class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = [-1]

        prevSmaller = [0] * n
        nextSmaller = [0] * n

        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prevSmaller[i] = stack[-1]
            stack.append(i)

        stack = [-1]

        for i in range(n - 1, -1, -1):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            nextSmaller[i] = n if stack[-1] == -1 else stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            height = heights[i]
            width = nextSmaller[i] - prevSmaller[i] - 1
            maxArea = max(maxArea, height * width)

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        histogram = [0] * cols
        answer = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    histogram[j] = 0
            answer = max(answer, self.largestRectangleArea(histogram))

        return answer