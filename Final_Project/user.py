#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import pdb

FILE_PATH = '../fixtures/example.osm'
UID = "uid"

def get_user(element, users):

    if UID in element.attrib:
        users.add(element.attrib["uid"])
    return users


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
            get_user(element, users)

    return users


def test():

    users = process_map(FILE_PATH)
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()
