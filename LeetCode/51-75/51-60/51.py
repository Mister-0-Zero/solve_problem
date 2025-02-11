class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def func(n, iteration = 0, matrix = None, res = None):
            if matrix is None:
                matrix = [["." for _ in range(n)] for _ in range(n)]
            if res is None:
                res = []
            if iteration == n:
                res.append([''.join(matrix[i]) for i in range(n)])
                return
            for ind in range(n):
                if check(matrix, iteration, ind, n):
                    matrix[iteration][ind] = "Q"
                    func(n, iteration + 1, matrix, res)
                    matrix[iteration][ind] = "."
            return res

        def check(matrix, iteration, ind, n):
            for num_str in range(iteration):
                if matrix[num_str][ind] == "Q":
                    return False

            iteration_, ind_ = iteration, ind

            while iteration >= 0 and ind >= 0:
                if matrix[iteration][ind] == "Q":
                    return False
                iteration -= 1
                ind -= 1

            iteration, ind = iteration_, ind_

            while iteration >= 0 and ind < n:
                if matrix[iteration][ind] == "Q":
                    return False
                iteration -= 1
                ind += 1

            return True

        return func(n)

instance = Solution()
res = instance.solveNQueens(4)
print(res)

