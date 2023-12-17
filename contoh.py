# Add the project root to sys.path
import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

import sys
import os
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)
from util.time_measurement import time_function,  CodeTimer
#measure the line of code
with CodeTimer('bebas buat penanda'):
    for i in range(10):
        #do something
        pass
#measure function
@time_function   
def search():
   pass

import time
t1 = time.time()
i = 0

while i < len(nums):
  if nums[i] == target:
    return i
  i = i + 1
return i
t2=time.time()
time_execution = t2 - t1
print("time execution of this line of code: ", time_execution)