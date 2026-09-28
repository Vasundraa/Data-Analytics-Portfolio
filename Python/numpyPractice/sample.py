# marks=[88,90,30,45,75]
# copyMarks=marks.copy()
# for i in range(len(copyMarks)):
#     copyMarks[i]=copyMarks[i]+5

# print(marks)
# print(copyMarks)

import numpy as np
marks=np.array([88,90,30,45,75])
copyMarks=marks.copy()
copyMarks=copyMarks+5
print(marks)
print(copyMarks)