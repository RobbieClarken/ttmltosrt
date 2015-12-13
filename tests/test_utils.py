from ttmltosrt.ttmltosrt import parse_time, format_timedelta
from datetime import timedelta


def test_parse_time():
    assert parse_time('552400000t', 10000000) == timedelta(0, 55, 240000)


def test_format_timedelta():
    assert format_timedelta(timedelta(0, 55, 240000)) == '00:00:55,240'
