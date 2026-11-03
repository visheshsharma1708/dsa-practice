
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Store building start positions
        starts = {}
        positions = set()

        for left, right, height in buildings:
            starts.setdefault(left, []).append((height, right))
            positions.add(left)
            positions.add(right)

        # Max heap: (-height, right)
        # Initially, ground height 0 is active
        heap = [(0, float('inf'))]

        result = []
        prev_height = 0

        for x in sorted(positions):
            # Add all buildings that start at x
            for height, right in starts.get(x, []):
                heapq.heappush(heap, (-height, right))

            # Remove buildings that have ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Current maximum height
            curr_height = -heap[0][0]

            # Add a key point only when height changes
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height

        return result
