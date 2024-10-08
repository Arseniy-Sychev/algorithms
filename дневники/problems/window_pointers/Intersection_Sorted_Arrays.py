'''
Find the intersection of two sorted arrays OR in other words, 
given 2 sorted arrays, find all the elements which occur in both arrays.

NOTE: For the purpose of this problem ( as also conveyed by the sample case ), 
assume that elements that appear more than once in both arrays should be included 
multiple times in the final output.
'''

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
		p1 = 0
		p2 = 0
		result = []
		while p1 < len(A) and p2 < len(B):
			if A[p1] == B[p2]:
				result.append(A[p1])
				p1 += 1
				p2 += 1
			elif A[p1] < B[p2]:
				p1 += 1
			elif A[p1] > B[p2]:
				p2 += 1
		return result