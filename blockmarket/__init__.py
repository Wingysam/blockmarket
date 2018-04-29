DEFAULTTEXT = '\033[0m'
BLACKTEXT = '\033[30m'
REDTEXT = '\033[31m'
GREENTEXT = '\033[32m'
YELLOWTEXT = '\033[33m'
BLUETEXT = '\033[34m'
MAGENTATEXT = '\033[35m'
CYANTEXT = '\033[36m'
WHITETEXT = '\033[37m'

try:
    import requests
except:
    print(REDTEXT + 'Could not import requests.' + DEFAULTTEXT)
try:
    import json
except:
    print(REDTEXT + 'Could not import json.' + DEFAULTTEXT)
try:
    from html.parser import HTMLParser
except:
    print(REDTEXT + 'Could not import html.parser.' + DEFAULTTEXT)

class items:
    def dict():
        global ctag
        global printdata
        global jsoncode
        ctag = ''
        printdata = False
        jsoncode = '{'

        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                True
                global ctag
                global printdata
                ctag = tag
                if tag == 'a':
                    printdata = True
                else:
                    printdata = False
            def handle_endtag(self, tag):
                True

            def handle_data(self, data):
                True
                global ctag
                global printdata
                if printdata and not data == 'THEBLOCKHEADS.NET' and not data == 'WHAT IS THIS?' and not data == '\n':
                    if ctag == 'a':
                        global jsoncode
                        jsoncode = jsoncode + '"' + data + '":'
                elif '.' in data and not '.NET' in data:
                    jsoncode = jsoncode + data + ','

        parser = MyHTMLParser()
        parser.feed(requests.get('http://blockmarket.theblockheads.net/').text)

        jsoncode = jsoncode[:-1] + '}'

        items = json.loads(jsoncode)

        return(items)

    def json():
        global ctag
        global printdata
        global jsoncode
        ctag = ''
        printdata = False
        jsoncode = '{'

        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                True
                global ctag
                global printdata
                ctag = tag
                if tag == 'a':
                    printdata = True
                else:
                    printdata = False
            def handle_endtag(self, tag):
                True

            def handle_data(self, data):
                True
                global ctag
                global printdata
                if printdata and not data == 'THEBLOCKHEADS.NET' and not data == 'WHAT IS THIS?' and not data == '\n':
                    if ctag == 'a':
                        global jsoncode
                        jsoncode = jsoncode + '"' + data + '":'
                elif '.' in data and not '.NET' in data:
                    jsoncode = jsoncode + data + ','

        parser = MyHTMLParser()
        parser.feed(requests.get('http://blockmarket.theblockheads.net/').text)

        jsoncode = jsoncode[:-1] + '}'

        return(jsoncode)
