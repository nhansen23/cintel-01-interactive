import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Requirement 1: Page title
ui.page_opts(title="My Browser Interactive App", fillable=True)

# Requirement 2: interactive input slider
# 5 arguments required:
# string id that identifies the input value
# string label for display
# int for min number of bins
# int for max number of bins
# int for initial slider value
with ui.sidebar():
  ui.input_slider("number_of_bins", "Number of Bins", 0, 50, 25)


# Requirement 3: reactive output chart
# pass numpy data array
# pass user input of number of bins
# set density to True
@render.plot(alt="A histogram")
def draw_histogram():
  count_of_points: int = 437
  np.random.seed(10)
  random_data_array = 100 + 15 * np.random.randn(count_of_points)
  plt.hist(random_data_array, input.number_of_bins(), density=True)
  random_data_array = 100 + 15 * np.random.randn(count_of_points)
  plt.hist(random_data_array, input.number_of_bins(),density=True)

