class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.matrix = None
            return 
        self.matrix = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]

        self.matrix[0][0] = matrix[0][0]
        
        for i in range(1,len(matrix)):
            self.matrix[i][0] = self.matrix[i-1][0] + matrix[i][0]
        for j in range(1,len(matrix[0])):
            self.matrix[0][j] = self.matrix[0][j-1] + matrix[0][j]
        
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                 self.matrix[i][j] = self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1] + matrix[i][j]
                    
        
        
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 
        return self.matrix[row2][col2]+(self.matrix[row1-1][col1-1] if row1>0 and col1>0 else 0)-(self.matrix[row2][col1-1] if col1>0 else 0)-(self.matrix[row1-1][col2] if row1>0 else 0)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
