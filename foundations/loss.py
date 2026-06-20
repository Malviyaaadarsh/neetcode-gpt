import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        epsilon = (1e-7)
        L = -np.sum(y_true*np.log(y_pred+epsilon) + (1-y_true)*np.log(1-y_pred + epsilon))/len(y_true)
        return np.round(L,4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        epsilon = (1e-7)
        L = -np.sum(np.sum(y_true*np.log(y_pred+epsilon)))/len(y_true)
        return np.round(L,4)

