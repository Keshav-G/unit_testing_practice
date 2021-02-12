# Test the function that finds the slope of the line
test_find_slope():
	from point_on_line import find_slope
	slope = find_slope((0, 0), (1, 1))
	expected = 1
	assert slope == expected

# Test the function that finds the y-intercept of the line
test_find_y_intercept():
	from point_on_line import find_y_intercept
	y_intercept = find_y_intercept((0, 0), 1)
	expected = 0
	assert y_intercept == expected

# Test the function that calculates the y value for the input x value
test_return_y_value():
	from point_on_line import return_y_value
	y_value = return_y_value(1, 0, -5)
	expected = -5
	assert y_value == expected

	
