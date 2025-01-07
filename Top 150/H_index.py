class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
         # Sort citations in descending order
        citations.sort(reverse=True)
    
        h = 0  # Initialize h-index
        for i in range(len(citations)):
            # Check if the current paper satisfies the h-index condition
            if i + 1 <= citations[i]:
                h = i + 1  # Update h-index
            else:
                break  # No need to check further
        
        return h
