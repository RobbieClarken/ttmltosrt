from ttmltosrt import srt_generator


def test_srt_generator():
    ttml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        '<tt xmlns:tt="http://www.w3.org/ns/ttml" ttp:tickRate="10000000">'
        '<body>'
        '<div xml:space="preserve">'
        '<p begin="552400000t" end="601200000t" xml:id="subtitle0">Caption 1</p>'
        '<p begin="992000000t" end="1014800000t" xml:id="subtitle1">Caption 2</p>'
        '</div>'
        '</body>'
        '</tt>'
    )
    srt_captions = list(srt_generator(ttml))
    assert len(srt_captions) == 2
    assert srt_captions[0] == '1\n00:00:55,240 --> 00:01:00,120\nCaption 1\n'


def test_srt_generator_without_tickrate():
    ttml = (
        '<?xml version="1.0" encoding="utf-8" ?>'
        '<tt xml:lang="en" xmlns="http://www.w3.org/ns/ttml" '
        '    ttp:profile="http://www.w3.org/TR/profile/sdp-us" >'
        '<body>'
        '<div>'
        '<p begin="00:00:55.240" end="00:01:00.120">Caption 1</p>'
        '</div>'
        '</body>'
        '</tt>'
    )
    srt_captions = list(srt_generator(ttml))
    assert srt_captions[0] == '1\n00:00:55,240 --> 00:01:00,120\nCaption 1\n'


def test_srt_generator_with_incomplete_milliseconds():
    ttml = (
        '<?xml version="1.0" encoding="utf-8" ?>'
        '<tt xml:lang="en" xmlns="http://www.w3.org/ns/ttml" '
        '    ttp:profile="http://www.w3.org/TR/profile/sdp-us" >'
        '<body>'
        '<div>'
        '<p begin="00:00:55.24" end="00:01:00.12">Caption 1</p>'
        '</div>'
        '</body>'
        '</tt>'
    )
    srt_captions = list(srt_generator(ttml))
    assert srt_captions[0] == '1\n00:00:55,240 --> 00:01:00,120\nCaption 1\n'


def test_srt_generator_with_dur_attribute():
    ttml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<tt xml:lang="no" xmlns="http://www.w3.org/ns/ttml" '
        '    xmlns:tts="http://www.w3.org/ns/ttml#styling">'
        '  <head>'
        '    <styling>'
        '      <style xml:id="italic" tts:fontStyle="italic" />'
        '      <style xml:id="left" tts:textAlign="left" />'
        '      <style xml:id="center" tts:textAlign="center" />'
        '      <style xml:id="right" tts:textAlign="right" />'
        '    </styling>'
        '  </head>'
        '  <body>'
        '    <div>'
        '      <p begin="00:00:00.000" dur="00:00:00.000">Caption 1</p>'
        '      <p begin="00:00:01.234" dur="00:00:02.345" style="left">Caption 2</p>'
        '    </div>'
        '  </body>'
        '</tt>'
    )
    srt_captions = list(srt_generator(ttml))
    assert srt_captions[0] == '1\n00:00:00,000 --> 00:00:00,000\nCaption 1\n'
    assert srt_captions[1] == '2\n00:00:01,234 --> 00:00:03,579\nCaption 2\n'
