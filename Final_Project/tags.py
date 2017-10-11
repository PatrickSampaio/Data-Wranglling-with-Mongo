import xml.etree.cElementTree as ET
import pprint
import re
import pdb

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CONST_LOWER = 'lower'
CONST_LOWER_COLON = 'lower_colon'
CONST_OTHER = 'other'
CONST_PROBLEMCHARS = 'problemchars'
CONST_ATTRIBUTE = 'k'

def key_type(element, keys):

    if element.tag == "tag":
       pdb.set_trace()
       if problemchars.match(element.attrib[CONST_ATTRIBUTE]) is not None:
           keys[CONST_PROBLEMCHARS] = keys[CONST_PROBLEMCHARS] + 1
       elif lower_colon.match(element.attrib[CONST_ATTRIBUTE]) is not None:
           keys[CONST_LOWER_COLON] = keys[CONST_LOWER_COLON]
       elif lower.match(element.attrib[CONST_ATTRIBUTE]) is not None:
           keys[CONST_LOWER] = keys[CONST_LOWER] + 1
       else:
           keys[CONST_OTHER] = keys[CONST_OTHER] + 1
        
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    keys = process_map('../fixtures/example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()
