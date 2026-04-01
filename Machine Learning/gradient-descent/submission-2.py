class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        ans = init
        for i in range(iterations):
            ans = ans - learning_rate * 2 * ans
        return round(ans, 5)
