    from xml.etree import cElementTree as ElementTree
    import nltk
    import pandas as pd

    tree = ElementTree.parse('/Volumes/Samsung_T5/ODISSEI/DANS_example.xml')
    root = tree.getroot()

    Base = '{http://www.openarchives.org/OAI/2.0/}'
    kernel4 = '{http://datacite.org/schema/kernel-4}'
    path = f'./{Base}ListRecords/{Base}record/*/*/'

    def chunkfinder(parsed, path = path):
        for target in parsed.findall(path):
            print(target.text)

    chunkfinder(root)
