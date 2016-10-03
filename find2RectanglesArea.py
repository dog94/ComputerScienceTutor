"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner.

        -------- (C,D)
        |      |
        |  ------- (G,H)
        |  |   | |
        |  |   | |
  (A,B) ---|---- |
           |     |
     (E,F) -------
"""



class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """ 
        # when one of the rectangle has area of 0
        if((D-B)*(A-C)==0):
            return (G-E)*(H-F)
        if((G-E)*(H-F)==0):
            return (A-C)*(B-D)
            
        # when there is no overlapping
        if(max(A,C)<min(E,G) or max(E,G)<min(A,C) or max(B,D)<min(H,F)or max(H,F)<min(B,D)):
            return ((A-C)*(B-D) + (G-E)*(H-F))
            
        # when they overlap, find the 2 points in the middle that define the inner rectangle
        x=[A,C,E,G]
        y=[B,D,F,H]
        x.sort()
        y.sort()
        #subtract the overlapped area
        return (G-E)*(H-F)+(A-C)*(B-D)-(x[2]-x[1])*(y[2]-y[1])