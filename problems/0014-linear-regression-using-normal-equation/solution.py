import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	import numpy as np
	X_t = np.transpose(X)
	X_t_X = np.matmul(X_t, X)
	inv_X_t_X = np.linalg.inv(X_t_X)
	
	return np.matmul(inv_X_t_X, X_t) @ y
