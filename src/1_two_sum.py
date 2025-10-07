class Solution(object):
    def getIndices(self, array: list, target: int):
        """
        - Traverse the array
        - diff = target - element, check for the condition
        - j must start from i + 1
        - add tuple to the list.
        - Worse case time complexity is still higher(On^2)
        """
        results = []
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if array[j] == target - array[i]:
                    results.append((i, j))
        return results
    
    def getIndicesBetter(self, array: list, target: int):
        """HashMap Approach

        - an empty dict
        - Traverse through the list and add vale:index list
        - use the difference = target - array[i]
        - get the indices directly.

        """
        results = []
        trackerDict = {} # value : index

        for i in range(len(array)):
            diff = target - array[i]
            if diff in trackerDict:
                results.append((trackerDict[diff], i))
            trackerDict[array[i]] = i
        return results
    
            


    
if __name__ == "__main__":
    solution = Solution()

    print(f"Array lenth: 2")
    print(f"Indices: {solution.getIndices([3,3], 6)}")
    print(f"Array lenth: 3")
    print(f"Indices: {solution.getIndices([5,3,3], 6)}")
    print(f"Array lenth: 4")
    print(f"Indices: {solution.getIndices([2,5,3,3], 6)}")
    print(f"Array lenth: 5")
    print(f"Indices: {solution.getIndices([-1,2,5,3,3], 6)}")

    print(f"Array lenth: 2")
    print(f"Indices: {solution.getIndicesBetter([3,3], 6)}")
    print(f"Array lenth: 3")
    print(f"Indices: {solution.getIndicesBetter([5,3,3], 6)}")
    print(f"Array lenth: 4")
    print(f"Indices: {solution.getIndicesBetter([2,5,3,3], 6)}")
    print(f"Array lenth: 5")
    print(f"Indices: {solution.getIndicesBetter([-1,2,5,3,3], 6)}")
    