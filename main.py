import matplotlib.pyplot as plt1
import spacy

from collections import Counter

"""https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list"""
nlp = spacy.load("en_core_web_sm")
print("chose between Bicycles : 1 and Highlights_of_the_Prado_Museum.xml : 2 as the File")
t = input('Input:')
if t == "1":
    f = open("training/Traning/RFC/Bicycles.xml", "r")
elif t == "2":
    f = open("training/Traning/ANC/WhereToMadrid/Highlights_of_the_Prado_Museum.xml", "r")
temp = f.read()
doc = nlp(temp)


def pos():
    """Wie oft kommen welche PoS-Tags vor?"""
    pos_list = []
    for token in doc:
        pos_list.append(token.pos_)
    setList = list(set(pos_list))
    my_dict = {i: pos_list.count(i) for i in setList}
    print(my_dict)


def tag():
     """Wie viele [SpatialEntities, Places, Motions, Locations, Signals, QsLinks, OLinks] gibt es?"""
     iso_list = []
     tags = ["spatial_entity", "place", "motion", "location", "signal", "qslink", "olink"]
     for token in doc:
        if token.norm_ in tags:
               iso_list.append(token.norm_)
     setList = list(set(iso_list))
     my_dict = {i: iso_list.count(i) for i in setList}

     for i in tags:
         if i.lower() not in my_dict:
            my_dict[i] = 0
     print(my_dict)

def qsl():
    """Wie oft kommen welche QsLink Typen vor? (DC,EC, ...)?"""
    new_line = temp.splitlines()
    qs_line = []
    reltype = []
    for i in range(len(new_line)):
        if "QSLINK" in new_line[i]:
            qs_line.append(new_line[i].split('" '))
    for i in range(len(qs_line)):
        reltype.append(qs_line[i][5].split('="')[1])
    setList = list(set(reltype))
    my_dict = {i: reltype.count(i) for i in setList}
    print(my_dict)

def satz():
    new_line = temp.split("TEXT")
    new_line[1] = new_line[1].replace("><![CDATA[", "")
    new_line[1] = new_line[1].replace("]]></", "")
    new_line[1] = new_line[1].replace("\n", "")
    ea_sentence = new_line[1].split(". ")

    for i in range(len(ea_sentence)):
        ea_sentence[i] = ea_sentence[i].split(" ")
    len_sentence = []

    for i in ea_sentence:
        len_sentence.append(len(i))

    setList = list(set(len_sentence))
    my_dict = {i: len_sentence.count(i) for i in setList}
    temp_len = []
    temp_times = []

    for i in my_dict:
        temp_len.append(i)
        temp_times.append(my_dict[i])
    plt.xlabel("Nummber of Words")
    plt.ylabel("Amount of Sentence with x Words  ")
    plt.bar(temp_len, temp_times)
    plt.xticks(temp_len, temp_len)
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=1, wspace=0, hspace=0)
    plt.show()


def prob():
    """Welche Links (QSLinks, OLinks) werden von welchen Präpositionen (markiert durch SPATIAL_SIGNAL) getriggert (z.B. wie oft werden QSLinks durch die Präposi"""
    new_line = temp.splitlines()
    links_line = []
    trigger = []

    spac_link = []
    for i in range(len(new_line)):
        if "QSLINK" in new_line[i] or "OLINK" in new_line[i]:
            links_line.append(new_line[i].split('" '))

    for i in range(len(links_line)):
        temp1 = links_line[i][0].split("=")
        temp2 = links_line[i][8].split("=")
        if "s" in temp2[1]:
            spac_link.append((temp1[1] + '"', temp2[1] + '"'))
        trigger.append(links_line[i][8].split('="')[1])
    print(spac_link)
    setList = list(set(trigger))
    my_dict = {i: trigger.count(i) for i in setList}
    print(my_dict)

def verb():
    """Welches sind die fünf häufigsten „MOTION“ Verben (und wie oft kommen diese vor)"""

    new_line = temp.splitlines()
    q_line = []
    trigger = []
    for i in range(len(new_line)):
        if "MOTION" in new_line[i]:
            q_line.append(new_line[i].split('" '))

    for i in range(len(q_line)):
        trigger.append(q_line[i][3].split('="')[1])

    setList = list(set(trigger))
    my_dict = {i: trigger.count(i) for i in setList}
    print(dict(Counter(my_dict).most_common(5)))

while(True):
    print("Gültige eingabe ist nur eine Zahl!!!!")
    print("Bitte wählen Zwichen 2.3.1 bis 2.3.6  mit 1 bis 6 aus.")
    print("Mit einer ungültigen eingabe wird das Programm beendet!!!")
    t = input('Input:')
    if t == "1":
        pos()
    elif t == "2":
        tag()
    elif t == "3":
        qsl()
    elif t == "4":
        satz()
    elif t == "5":
        prob()
    elif t == "6":
        verb()
    else:
        exit()
