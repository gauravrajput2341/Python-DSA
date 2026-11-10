
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        left,right = 0, len(matrix[0])-1
        top , down = 0, len(matrix) -1
        if not matrix or not matrix[0]:
            return result

        while top<= down and left <= right:
            for i in range (left ,right + 1):
                result.append(matrix[top][i])
            top +=1
            for i in range(top,down + 1):
                result.append(matrix[i][right])
            right -= 1
            if top<= down:
                for i in range (right,left - 1, -1):
                    result.append(matrix [down][i])            
                down -=1
            if left<=right:
                for i in range(down,top - 1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result