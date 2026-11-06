
class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:

        # Calculate total candies
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        # Calculate the difference
        diff = (bob_total - alice_total) // 2

        # Store Bob's candy boxes in a set
        bob_set = set(bobSizes)

        # Find the correct exchange
        for x in aliceSizes:
            y = x + diff

            if y in bob_set:
                return [x, y]
