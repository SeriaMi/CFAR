import sys
import os

# 添加 DBReader 的路径
sys.path.append(os.path.abspath(r"E:\工作日志\Git\RADIal\DBReader"))

from DBReader.DBReader import SyncReader, ASyncReader

print(os.getcwd())
print("Hello World!")