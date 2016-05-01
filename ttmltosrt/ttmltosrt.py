#!/usr/bin/env python3

from datetime import timedelta
import re

from bs4 import BeautifulSoup
import click


@click.command()
@click.argument('in_file', type=click.File('r'))
@click.argument('out_file', type=click.File('w'), required=False)
def convert_file(in_file, out_file=None):
    for srt in srt_generator(in_file.read()):
        print(srt, file=out_file)


def srt_generator(ttml):
    soup = BeautifulSoup(ttml, 'html.parser')
    try:
        tick_rate = float(soup.tt['ttp:tickrate'])
    except KeyError:
        tick_rate = None
    captions = soup.body.find_all('p')
    for caption_number, caption in enumerate(captions, start=1):
        begin = parse_time(caption['begin'], tick_rate)
        end = parse_time(caption['end'], tick_rate)
        yield '{n}\n{begin} --> {end}\n{content}\n'.format(
            n=caption_number,
            begin=format_timedelta(begin),
            end=format_timedelta(end),
            content=caption.get_text(separator='\n')
        )


def parse_time(time_str, tick_rate=None):
    if time_str.endswith('t'):
        return timedelta(seconds=float(time_str.rstrip('t')) / tick_rate)
    match = re.search('(\d\d):(\d\d):(\d\d).(\d\d\d)', time_str)
    h, m, s, ms = (int(s) for s in match.groups())
    return timedelta(hours=h, minutes=m, seconds=s, milliseconds=ms)


def format_timedelta(t):
    return '{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'.format(
        hours=t.seconds // 3600,
        minutes=t.seconds // 60 % 60,
        seconds=t.seconds % 60,
        milliseconds=t.microseconds // 1000,
    )


if __name__ == '__main__':
    convert_file()
