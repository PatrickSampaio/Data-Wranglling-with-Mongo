import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"

PATH_TO_AUTHOR = "./fm/bibl/aug/au"

FNM_FIELD = "fnm"
SNM_FIELD = "snm"
EMAIL_FIELD = "email"
INSR_FIELD = "insr"
INSR_ID_ATTRIBUTE = "iid"



def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall(PATH_TO_AUTHOR):
        data = {
            FNM_FIELD: author.find(FNM_FIELD).text,
            SNM_FIELD: author.find(SNM_FIELD).text,
            EMAIL_FIELD: author.find(EMAIL_FIELD).text,
            INSR_FIELD: [insr.get(INSR_ID_ATTRIBUTE) for insr in author.findall(INSR_FIELD)]
        }
        authors.append(data)

    return authors


def test():
    solution = [{'insr': ['I1'], 'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'},
                {'insr': ['I2'], 'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'},
                {'insr': ['I3', 'I4'], 'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'},
                {'insr': ['I3'], 'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'},
                {'insr': ['I8'], 'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'},
                {'insr': ['I3', 'I5'], 'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'},
                {'insr': ['I6'], 'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'},
                {'insr': ['I7'], 'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]

    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["insr"] == solution[1]["insr"]


test()