import pandas as pd
import math
import numpy as np

l = list(range(10))
print(l)

# 对l中的每个元素开根号
# 使用map
result = map(math.sqrt, l)
print(result)


ser = pd.Series(l)

# 开根号
ser.map(np.sqrt)


# 自定义函数
ser.map(lambda x: x**2 + 1)


staff_df = pd.DataFrame([{'姓名': '张三', '部门': '研发部'},
                        {'姓名': '李四', '部门': '财务部'},
                        {'姓名': '赵六', '部门': '市场部'}])
staff_df
