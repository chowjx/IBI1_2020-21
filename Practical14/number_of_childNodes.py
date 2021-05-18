from xml.dom.minidom import parse 
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse('go_obo.xml')
obo = DOMTree.documentElement
terms = obo.getElementsByTagName('term')
defs = terms.getElementsByTagName('def')
for def in defs:
    if def.hasAttribute('defstr'):
        if