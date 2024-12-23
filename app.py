from flask import Flask
import random
import requests
import numpy as np


app = Flask(__name__)


def unused_function():
    print("I do nothing meaningful")

app = Flask(__name__)

@app.route("/")
def index():
    # 返回一些凌乱的信息
    value = np.random.randint(100)  # 实际上np也没必要用
    # 这里本可直接用random.random()就行，但我们刻意多此一举
    return f"Hello, this is a messy app! Random value: {value} - " \
           f"And maybe some unused stuff?"

# Another route (not really needed)
@app.route("/test")
def test():
    # 无用的复杂计算
    arr = np.array([1,2,3])
    val = arr.sum() + random.randint(0,10)
    return f"Test route, val: {val}"

if __name__ == "__main__":
    # 没有真正的日志配置、debug模式
    app.run(host="0.0.0.0", port=5000)
