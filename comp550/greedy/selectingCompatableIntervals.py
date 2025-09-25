class Solution:
    def zeroIndexifyIntervals(self, intervals):
        # Convert 1-indexed intervals to 0-indexed
        return [[start - 1, end - 1] for start, end in intervals]
    
    def selectCompatibleIntervals(self, intervals):
        """
        Select the maximum number of non-overlapping intervals.
        Intervals are given as list of [start, end] pairs (1-indexed).
        """
        if not intervals:
            return []
        
        # Convert to 0-indexed for processing
        intervals = self.zeroIndexifyIntervals(intervals)
        
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        selected = [intervals[0]]
        last_end = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] >= last_end:
                selected.append(interval)
                last_end = interval[1]
        
        # Convert back to 1-indexed for output
        selected_1_indexed = [[start + 1, end + 1] for start, end in selected]
        return selected_1_indexed


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: Basic example
    intervals1 = [[4, 36], [17, 147], [5, 18], [62, 67], [16, 32], [96, 128], [21, 117], [19, 122], [64, 168], [45, 99], [12, 55], [20, 26], [79, 126], [3, 9], [89, 101], [55, 112], [26, 157], [1, 2], [16, 116], [49, 70], [26, 60], [52, 153], [16, 28], [20, 83], [158, 166], [3, 7], [7, 8], [61, 140], [1, 4], [12, 170], [19, 57], [35, 110], [54, 155], [93, 137], [47, 58], [49, 114], [115, 174], [60, 61], [64, 90], [3, 142], [4, 145], [89, 119], [24, 76], [22, 154], [63, 108], [8, 27], [26, 49], [18, 77], [106, 175], [2, 87], [7, 148], [65, 66], [36, 135], [17, 118], [96, 130], [38, 171], [4, 40], [24, 38], [22, 132], [129, 144]]
    result1 = sol.selectCompatibleIntervals(intervals1)
    print("Test 1 - Intervals:", intervals1)
    print("Selected:", result1)
    print("Count:", len(result1))
    print()
    
    # Test case 2: Overlapping intervals
    intervals2 = [[1, 4], [2, 3], [4, 6], [5, 7]]
    result2 = sol.selectCompatibleIntervals(intervals2)
    print("Test 2 - Intervals:", intervals2)
    print("Selected:", result2)
    print("Count:", len(result2))
    print()
    
    # Test case 3: No overlaps
    intervals3 = [[1, 2], [3, 4], [5, 6]]
    result3 = sol.selectCompatibleIntervals(intervals3)
    print("Test 3 - Intervals:", intervals3)
    print("Selected:", result3)
    print("Count:", len(result3))
