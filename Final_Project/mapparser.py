import xml.etree.cElementTree as ET
import pprint
import pdb

PATH_TO_FILE = "../fixtures/example.osm"

def count_tags(filename):
    current_dict = {}
    line_count = 0
    for event, elem in ET.iterparse(filename):
        line_count = line_count + 1
        #if len([True for key in current_dict if current_dict[key] == elem.tag]) == 0:
        if elem.tag not in current_dict:
            current_dict[elem.tag] = line_count
    
    return current_dict

def test():

    tags = count_tags(PATH_TO_FILE)
    pprint.pprint(tags)

    

if __name__ == "__main__":
    test()
