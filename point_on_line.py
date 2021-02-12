# Functions to calculate the y-value on a line (specified by 2 chosen points)
#  for a specified x-input

# Find the slope of the line specified by the 2 points
def find_slope(point1, point2):

	# Unpack tuples
	x1, y1 = point1
	x2, y2 = point2

	# Find slope
	numerator = y2 - y1
	denominator = x2 - x1
	slope = numerator / denominator
	return slope


# Calculate the slope of the line
def find_y_intercept(point1, slope):
	
	# Unpack tuple
	x1, y1 = point1
	
	# Find y-intercept
	y_intercept = y1 - (x1 * slope)
	return y_intercept

# Return the y value (on the line specified by the two points) for the specified x input
def return_y_value(slope, y_intercept, x_input):
	y_value = (slope * x_input) + y_intercept
	return y_value

