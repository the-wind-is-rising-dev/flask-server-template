# flask-server-template

Python 的 Flask 服务模版

## 模版功能

- 统一返回数据格式
- 统一为返回数据设置对象的 json 编解码器
- 日志同时输出至控制台、文件，日志文件自动截断
- 统一捕获异常信息
- 请求耗时统计
- 跨域支持
- 请求和响应日志记录

## 项目结构

```
flask-server-template/
├── config/
│   ├── __init__.py
│   └── log_config.py       # 日志配置
├── controller/
│   ├── __init__.py
│   ├── result.py           # 统一返回结果类
│   └── test_controller.py  # 测试控制器
├── service/
│   └── __init__.py
├── utils/
│   ├── __init__.py
│   ├── json_codec.py       # 自定义 JSON 编解码器
│   └── date_util.py        # 时间转换工具
├── .gitignore
├── application.py          # 应用入口
├── LICENSE
└── README.md
```

## 快速开始

### 运行项目

```bash
# 安装依赖
pip install flask flask-cors numpy

# 运行应用
python -m application
```

应用将在 `http://0.0.0.0:5001` 运行

## 核心功能说明

### 1. 统一返回数据格式

使用 `Result` 类统一返回数据格式，包含以下字段：

- `success`: 布尔值，表示请求是否成功
- `result`: 任意类型，请求成功时返回的数据
- `message`: 字符串，请求失败时返回的错误信息

示例使用：

```python
from controller import Result

# 返回成功结果
return Result.success("操作成功")

# 返回失败结果
return Result.fail("操作失败")
```

### 2. 自定义 JSON 编解码器

支持自动转换以下类型：

- `datetime`: 转换为 `%Y-%m-%d %H:%M:%S` 格式字符串
- `Enum`: 转换为枚举名称字符串
- `numpy.ndarray`: 转换为列表
- `numpy.integer`: 转换为 Python 整数
- `numpy.floating`: 转换为 Python 浮点数

### 3. 日志系统

- 日志同时输出至控制台和文件
- 日志文件自动截断，最大 100MB，超过后保留最新的 99MB
- 包含时间戳、线程名称、日志内容
- 支持重定向 `print` 输出

### 4. 统一异常处理

自动捕获未处理的异常，并返回统一的错误格式

### 5. 请求和响应日志

- 记录请求路径、方法、头信息、参数和请求体
- 记录响应状态码、耗时和响应结果
- 长请求体和响应结果自动截断

### 6. 跨域支持

默认支持所有跨域请求，可通过配置自定义跨域规则

### 7. 时间转换工具

提供了丰富的时间转换功能，包括：

- 字符串与 datetime/struct_time 类型转换
- datetime 与 struct_time 类型互转
- 时间格式格式化
- 秒级和毫秒级时间戳获取

示例使用：

```python
from utils.date_util import (
    parse_datetime, format_datetime,
    timestamp_seconds, timestamp_milliseconds
)

# 将字符串转换为 datetime 对象
dt = parse_datetime('2025-12-29 00:00:00')

# 将 datetime 对象转换为字符串
str_time = format_datetime(dt, '%Y-%m-%d')

# 获取秒级时间戳
sec_ts = timestamp_seconds(dt)

# 获取毫秒级时间戳
ms_ts = timestamp_milliseconds(dt)
```

主要方法：

- `parse_datetime(times: str, format: str = DATE_TIME_FORMAT) -> datetime | None`: 将字符串转换为 datetime 对象
- `parse_struct_time(times: str, format: str = DATE_TIME_FORMAT) -> struct_time | None`: 将字符串转换为 struct_time 对象
- `format_datetime(times: datetime, format: str = DATE_TIME_FORMAT) -> str | None`: 将 datetime 对象转换为字符串
- `format_struct_time(time_struct: struct_time, format: str = DATE_TIME_FORMAT) -> str | None`: 将 struct_time 对象转换为字符串
- `format_time(times: datetime | struct_time, format: str = DATE_TIME_FORMAT) -> str | None`: 统一的时间格式化方法
- `timestamp_seconds(times: datetime | struct_time) -> int | None`: 获取秒级时间戳
- `timestamp_milliseconds(times: datetime | struct_time) -> int | None`: 获取毫秒级时间戳

## 开发指南

### 添加新的控制器

1. 在 `controller` 目录下创建新的控制器文件
2. 创建蓝图并注册路由
3. 在 `application.py` 中添加蓝图到注册列表

示例控制器：

```python
from flask import Blueprint
from controller import Result

new_bp = Blueprint('new', __name__, url_prefix='/new')


@new_bp.route('/example', methods=['GET'])
def example():
    return Result.success("这是一个新的接口")
```

### 添加服务层

在 `service` 目录下创建服务类，实现业务逻辑

### 配置文件

可以根据需要在 `config` 目录下添加配置文件

## 技术栈

- Python 3.x
- Flask
- flask-cors
- numpy

## 贡献

欢迎大家提 issues 和 pull requests，共同改进这个 Flask 服务模板！

## 许可证

MIT License
