from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

# Parsing XML file using DOM (Document Object Model)
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

# Find the row containing <defstr> & confirm the type of molecule described in that row.
def check_molecule(terms, molecule):
    check_list = []
    for term in terms:
        defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
        lines = defstr_text.data
        if molecule in lines:
            check_list.append(term)
    return check_list

def get_childNodes(term_id, ids):
    allChildren = []
    for element in ids:
        is_a = element.getElementsByTagName("is_a")
        if not is_a:
            allChildren.append(element)
        else:
            children_id = [child.childNodes[0].data for child in is_a]
            children = []
            for id in children_id:
                children.append(term_id[id])
            # recursive method to count all children
            allChildren.append(element)
            allChildren += get_childNodes(term_id, children)
    return allChildren

def count_childNodes(terms, molecule):
    term_id_dict = {}
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        term_id_dict[id] = term
    match_list = check_molecule(terms, molecule)
    count = len(get_childNodes(term_id_dict, match_list)) - len(match_list)
    return count

# Run the function to get the result for output
DNA = count_childNodes(terms, "DNA")
RNA = count_childNodes(terms, "RNA")
protein = count_childNodes(terms, "protein")
glycoprotein = count_childNodes(terms, " glycoprotein")

# Print the results as output
print("the number of childNodes for each DNA-related gene ontology term: " + str(DNA))
print("the number of childNodes for each RNA-related gene ontology term: " + str(RNA))
print("the number of childNodes for each protein-related gene ontology term: " + str(protein))
print("the number of childNodes for each glycoprotein-related gene ontology term: " + str(glycoprotein))

# Construct pie chart using matplotlib
molecules = {"DNA": DNA, "RNA": RNA,
             "Protein": protein, "Glycoprotein": glycoprotein}
labels = molecules.keys()
sizes = molecules.values()
explode =(0, 0, 0, 0)
fig1, ax1 = plt.subplots()    
# ax1.xx, xx denotes the operation to the figure
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
ax1.set(title ='The number of childNodes')

plt.show()