import math
import re

#通用工具

#转 int
# 获取字符串中数字并返回
def ToInt(cell):
    iArr = re.findall('\d+', cell)
    string2 = cell.encode('utf8')
    id = filter(str.isdigit, string2)

    if len(iArr) > 0:
        return int(iArr[0])
    # return math.nan
    return 0.0

# 强制转换成字符型
def ToString(cell):
    if isinstance(cell, str):
        return cell
    else:
        return str(cell)

# 强制转换成浮点型 字符型返回0
def ToDouble(cell):
    if isinstance(cell, float):
        return cell
    else:
        try:
            res=float(cell)
            return res
        except:
            # return math.nan
            return 0.0



    
