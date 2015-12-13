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
