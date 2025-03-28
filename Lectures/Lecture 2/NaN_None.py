# In pandas, a missing value (NA: not available)
# is mainly represented by nan (not a number).
# None is also considered a missing value.

import numpy as np
import pandas as pd

result = np.sqrt(-1.0)
print(f"The resulting value is '{result}' which has the datatype {type(result)}")

s_bad = pd.Series([1, None], dtype=object)
s_good = pd.Series([1, np.nan])

s_bad
s_good

# NaN as a numerical value, it is a float
# None is a NoneType (python data type)

none_value = None
try:
    result = none_value + 5
except TypeError as e:
    result = f"Error: {e}"
print(f"Result: {result}")

# NaN in arithmetic operations
nan_result = np.nan + 5
print(f"Result: {nan_result}")
