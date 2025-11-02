from dataclasses import dataclass
from socketserver import DatagramRequestHandler
from this import d
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> int:
        result = []
        m1 = matrix[0]