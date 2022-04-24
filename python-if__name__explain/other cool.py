# -*- coding: utf-8 -*-

# 呼叫自定義的modules (py檔)
from cool import cool_func

print('Call it remotely')
# 呼叫自定義的function
cool_func()

print(__name__)
