import xml.etree.cElementTree as xml

def parseXML(xml_file):
    tree = xml.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    # выводим все данные
    print("-" * 40)
    print("Парсинг XML используя ElementTree: ")
    print("-" * 40)

    for child in root:
        print(child.tag, child.attrib)
        if child.tag == "appointment":
            for step_child in child:
                print(step_child.tag)

    # получаем данные используя дочерние элементы.
    print("-" * 40)
    print("Обрабатываем дочерние элементы: ")
    print("-" * 40)

    for appointment in root.findall('serial'):
        for appt_child in appointment:
            print("%s=%s" % (appt_child.tag, appt_child.text))

    # вывод данных, где количество сезонов больше 3
    print("-" * 40)
    print("Обработка по количеству сезонов")
    print("-" * 40)

    for child in root.findall('serial'):
        season = int(child.get('season'))
        if season > 3:
            name = child.get('name')
            print(name, "( seasons:", season, ")")




if __name__ == "__main__":
    parseXML("serial_list.xml")
