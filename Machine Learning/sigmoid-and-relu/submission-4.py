import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        ans = 1 / (1 + pow(math.e, -z))
        ans = np.round(ans,5)
        return ans

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.maximum(0, z)
