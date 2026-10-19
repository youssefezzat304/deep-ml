def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	axis = {"column": 0, "row": 1}
	return np.mean(matrix, axis=axis[mode])