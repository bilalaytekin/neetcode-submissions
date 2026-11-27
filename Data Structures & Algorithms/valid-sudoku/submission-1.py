class Solution:
    def isValid(self, section):
        counts = [0]*(ord('9')-ord('.')+1)
        for num in section:
            if num != '.':
                if counts[ord(num)-ord('.')] != 0:
                    print(section)
                    return False
                counts[ord(num)-ord('.')] += 1
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [['' for _ in range(3)]*3 for _ in range(3)]
        columns = ['' for _ in range(9)]
        for i in range(9):
            for j in range(9):
                boxes[i//3][j//3] += board[i][j]
                columns[j] += board[i][j]
        
        return all(
            self.isValid(board[i][:])
            and
            self.isValid(columns[j])
            and
            self.isValid(boxes[i%3][j%3])
            for i in range(9)
            for j in range(9)
            )