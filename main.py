import os
import os.path
import sys

from lxml import etree

def main (file_name):
    parser = etree.XMLParser (attribute_defaults = True, dtd_validation = True)
    tree   = etree.parse (file_name, parser)

    walk (tree.getroot (), 0)


def walk (element, indentation):
    print (" " * indentation + element.tag)

    for ( name, value ) in sorted (element.items ()):
        print (" " * (indentation + 3) + ":" + name + " = \"" + value + "\"")

    for child in element:
        walk (child, indentation + 3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            # XML_CATALOG_FILES is a space-separated list of URLs.
            #
            catalogs = os.environ["XML_CATALOG_FILES"].split (" ") if "XML_CATALOG_FILES" in os.environ else [ ]
            catalogs.append (os.path.abspath (sys.argv[2]))
            os.environ["XML_CATALOG_FILES"] = " ".join (catalogs)

        main (sys.argv[1])

    else:
        print ("ERROR: An input file name must be specified on the command-line.")
