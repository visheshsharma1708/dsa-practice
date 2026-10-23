
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        power = abs(n)

        if n < 0:
            x = 1.0 / x

        while power > 0:
            if power % 2 == 1:
                result *= x

            x *= x
            power //= 2

        return round(result, 5)
