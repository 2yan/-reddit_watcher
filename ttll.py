def t_to_l(text):
    text = text.lower()
    things = {
        'a':'4',
        'b':'8',
        'c':'(',
        'd':'|)',
        'e':'3',
        'f':'|=',
        'g':'6',
        'h':'#',
        'i':'i',
        'j':'J',
        'k':'|<',
        'l':'L',
        'm':'//.',
        'n':'^',
        'o':'0',
        'p':'|>',
        'q':'0,',
        'r':'2',
        's':'5',
        't':'7',
        'u':'u',
        'v':'\\/',
        'w':'.//',
        'x':'><',
        'y':'`/',
        'z':'z',
    }
    for key in things.keys():
        text = text.replace(key, things[key])
    return text
