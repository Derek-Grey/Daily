import time
from functools import wraps
from loguru import logger

# 日志记录装饰器
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"开始执行 {func.__name__}...")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.error(f"执行 {func.__name__} 时出错: {e}")
            raise
        end_time = time.time()
        logger.info(f"执行 {func.__name__} 完成，耗时 {end_time - start_time:.2f} 秒")
        return result
    return wrapper

# 异常处理装饰器
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"执行 {func.__name__} 时出错: {e}")
            raise
    return wrapper

import pandas as pd
import pymongo
from urllib.parse import quote_plus

# 数据转换函数，将字符串转换为浮点数
def trans_str_to_float64(df: pd.DataFrame, exp_cols: list = None, trans_cols: list = None) -> pd.DataFrame:
    if trans_cols is None and exp_cols is None:
        trans_cols = df.columns
    if exp_cols is not None:
        trans_cols = list(set(df.columns) - set(exp_cols))
    df[trans_cols] = df[trans_cols].astype('float64')
    return df

# 获取MongoDB客户端连接函数（只读）
def get_client_U():
    user, pwd = 'Tom', 'tom'
    return pymongo.MongoClient(f"mongodb://{quote_plus(user)}:{quote_plus(pwd)}@192.168.1.99:29900/")