"""time Module in Python – Detailed Explanation

The time module in Python provides functions to work with time, such as:

Getting current time

Measuring execution time

Pausing program execution

Working with timestamps

It deals mainly with system time (seconds since Epoch).

What is Epoch Time?

Epoch time (also called Unix timestamp) is:

Number of seconds passed since 1 January 1970, 00:00:00 (UTC)"""

import time
print(time.time())
# Output: (example) 1701301234.567890

import time
current_time = time.time()
print(current_time)
# Output: (example) 1701301234.567890
# Converting Epoch to Readable Format
local_time = time.ctime(current_time)
print(local_time)
# Output: (example) 'Mon Nov 29 12:34:56 2021'
# time.ctime() converts epoch time to a human-readable string format.

import time

print("Start")
time.sleep(3)   # pauses for 3 seconds
print("End")
# Output:
# Start
# (waits for 3 seconds)
# End


import time
t = time.localtime()
print(t)
# Output: time.struct_time(tm_year=2021, tm_mon=11, tm_mday=29, tm_hour=12, tm_min=34, tm_sec=56, tm_wday=0, tm_yday=333, tm_isdst=0)
# time.localtime() returns the current local time as a struct_time object.



import time
t = time.localtime()
formatted = time.strftime("%d-%m-%Y %H:%M:%S", t)
print(formatted)
# Output: (example) '29-11-2021 12:34:56'
# time.strftime() formats a struct_time into a readable string based on the specified format.
"""Common strftime Format Codes:
| Code | Meaning   |
| ---- | --------- |
| `%Y` | Year      |
| `%m` | Month     |
| `%d` | Day       |
| `%H` | Hour (24) |
| `%M` | Minute    |
| `%S` | Second    |
| `%a` | Weekday   |
| `%b` | Month Name|
"""


import time
date_str = "23-12-2025"
t = time.strptime(date_str, "%d-%m-%Y")
print(t)
# Output: time.struct_time(tm_year=2025, tm_mon=12, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=357, tm_isdst=-1)
# time.strptime() parses a string representing a time according to a format and returns a struct_time


# Measuring Execution Time ⏱️
# Example: Measure function runtime
import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()
print("Execution Time:", end - start)

# Output: Execution Time: (example) 0.023456096649169922
# This measures the time taken to execute a loop of 1,000,000 iterations.
