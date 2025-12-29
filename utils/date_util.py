import time
from datetime import datetime
from time import struct_time

DATE_TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


def parse_struct_time(times: str, format: str = DATE_TIME_FORMAT) -> struct_time | None:
    """
    将时间字符串转换成struct_time
    :param times: 时间字符串
    :param format: 时间格式
    :return: struct_time
    """
    if not times:
        return None
    return time.strptime(times, format)


def parse_datetime(times: str, format: str = DATE_TIME_FORMAT) -> datetime | None:
    """
    将时间字符串转换成datetime
    :param times: 时间字符串
    :param format: 时间格式
    :return: datetime
    """
    if not times:
        return None
    return datetime.strptime(times, format)


def parse(times: str, format: str = DATE_TIME_FORMAT) -> datetime | None:
    """
    将时间字符串转换成datetime
    :param times: 时间字符串
    :param format: 时间格式
    :return: datetime
    """
    return parse_datetime(times, format)


def format_struct_time(time_struct: struct_time, format: str = DATE_TIME_FORMAT) -> str | None:
    """
    将struct_time转换成时间字符串
    :param time_struct: struct_time
    :param format: 时间格式
    :return: 时间字符串
    """
    if time_struct is None:
        return None
    return time.strftime(format, time_struct)


def format_datetime(times: datetime, format: str = DATE_TIME_FORMAT) -> str | None:
    """
    将datetime转换成时间字符串
    :param times: datetime
    :param format: 时间格式
    :return: 时间字符串
    """
    if times is None:
        return None
    return format_struct_time(times.timetuple(), format)


def format_time(times: datetime | struct_time, format: str = DATE_TIME_FORMAT) -> str | None:
    """
    将datetime转换成时间字符串
    :param times: datetime
    :param format: 时间格式
    :return: 时间字符串
    """
    if times is None:
        return None
    if isinstance(times, struct_time):
        return format_struct_time(times, format)
    if isinstance(times, datetime):
        return format_datetime(times, format)
    raise TypeError('times must be struct_time or datetime')


def timestamp_seconds_by_datetime(times: datetime) -> int | None:
    """
    获取秒级时间戳
    :param times:
    :return: 秒级时间戳
    """
    if times is None:
        return None
    return int(times.timestamp())


def timestamp_milliseconds_by_datetime(times: datetime) -> int | None:
    """
    获取毫秒级时间戳
    :param times:
    :return: 毫秒级时间戳
    """
    return int(times.timestamp() * 1000)


def timestamp_seconds_by_struct_time(times: struct_time) -> int | None:
    """
    获取秒级时间戳
    :param times:
    :return: 秒级时间戳
    """
    return int(time.mktime(times))


def timestamp_milliseconds_by_struct_time(times: struct_time) -> int | None:
    """
    获取毫秒级时间戳
    :param times:
    :return: 毫秒级时间戳
    """
    if times is None:
        return None
    return int(time.mktime(times) * 1000)


def timestamp_seconds(times: datetime | struct_time) -> int | None:
    """
    获取秒级时间戳
    :param times:
    :return: 秒级时间戳
    """
    if times is None:
        return None
    if isinstance(times, datetime):
        return timestamp_seconds_by_datetime(times)
    if isinstance(times, struct_time):
        return timestamp_seconds_by_struct_time(times)
    raise TypeError("times must be datetime or struct_time")


def timestamp_milliseconds(times: datetime | struct_time) -> int | None:
    """
    获取毫秒级时间戳
    :param times:
    :return: 毫秒级时间戳
    """
    if times is None:
        return None
    if isinstance(times, datetime):
        return timestamp_milliseconds_by_datetime(times)
    if isinstance(times, struct_time):
        return timestamp_milliseconds_by_struct_time(times)
    raise TypeError("times must be datetime or struct_time")


if __name__ == "__main__":
    times = '2025-12-29 00:00:00'  # 1766937600
    print(f'original times: {times}，timestamp: 1766937600')
    datetime_obj = parse_datetime(times)
    time_struct = parse_struct_time(times)
    print(f'parse_datetime: {datetime_obj}')
    print(f'parse_struct_time: {time_struct}')
    datetime_str = format_datetime(datetime_obj)
    time_struct_str = format_struct_time(time_struct)
    print(f'format_datetime: {datetime_str}')
    print(f'format_struct_time: {time_struct_str}')
    print(f'format_time(datetime):{format_time(datetime_obj)}')
    print(f'format_time(struct_time):{format_time(time_struct)}')

    print(f'\noriginal times: {times}，timestamp: 1766937600')
    timestamp = timestamp_milliseconds_by_struct_time(time_struct)
    print(f'timestamp_milliseconds_by_struct_time: {timestamp}')
    timestamp = timestamp_milliseconds_by_datetime(datetime_obj)
    print(f'timestamp_milliseconds_by_datetime: {timestamp}')
    timestamp = timestamp_milliseconds(time_struct)
    print(f'timestamp_milliseconds(struct_time): {timestamp}')
    timestamp = timestamp_milliseconds(datetime_obj)
    print(f'timestamp_milliseconds(datetime): {timestamp}')

    print(f'\noriginal times: {times}，timestamp: 1766937600')
    timestamp = timestamp_seconds_by_datetime(datetime_obj)
    print(f'timestamp_seconds_by_datetime: {timestamp}')
    timestamp = timestamp_seconds_by_struct_time(time_struct)
    print(f'timestamp_seconds_by_struct_time: {timestamp}')
    timestamp = timestamp_seconds(datetime_obj)
    print(f'timestamp_seconds(datetime): {timestamp}')
    timestamp = timestamp_seconds(time_struct)
    print(f'timestamp_seconds(struct_time): {timestamp}')
