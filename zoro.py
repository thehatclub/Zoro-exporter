# import required modules
from bs4 import BeautifulSoup
import xml.etree.ElementTree as gfg
import re


# reading content
file_name = input(
    "Please enter the relative path to the xml file: ")
file = open(file_name, "r")
contents = file.read()

# load xml
soup = BeautifulSoup(contents, 'xml')
# Create root
root = gfg.Element('myanimelist')
info = gfg.Element('myinfo')
root.append(info)
info_node = gfg.SubElement(info, 'user_export_type')
info_node.text = "1"
folders = soup.find_all('folder')


# Function that appends data to xml


def iter(links, stat):
    for i in range(len(links)):
        a1 = gfg.Element('anime')
        root.append(a1)

        a2 = gfg.SubElement(a1, "series_animedb_id")
        a2.text = links[i]

        a3 = gfg.SubElement(a1, "my_status")
        a3.text = stat
        a4 = gfg.SubElement(a1, "update_on_import")
        a4.text = "1"


# Loop through each instance for all the ids
for j in range(len(folders)):
    ids = []
    f = BeautifulSoup(str(folders[j]), 'xml')
    links = f.find_all('link')
    stat = f.find("name").text
    countj = 0
    for i in range(len(links)):
        # find the numbers in the link node
        temp = re.findall(r'\d+', links[i].text)
        ids.append(temp[0])
    # call iter function to append to new xml file
    iter(ids, stat)

tree = gfg.ElementTree(root)
with open("export.xml", "wb") as files:
    tree.write(files)
print("Completed! Saved to export.xml\n-------------------------------\nPython Script made by Zeldasman")
