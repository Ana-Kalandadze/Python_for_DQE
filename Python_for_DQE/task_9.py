import xml.etree.ElementTree as ET


def create_xml(results):

    news_log = ET.Element('news_log')

    # Split results into lines
    lines = results.split('\n')

    # For every four lines, create a new 'news' element
    for i in range(0, len(lines), 4):
        news = ET.SubElement(news_log, 'news')
        news_type = ET.SubElement(news,'type')
        news_type.text = lines[i].split('----------')[0]

        news_content = ET.SubElement(news, 'content')
        news_content.text = lines[i+1]

    # Write XML to file
    tree = ET.ElementTree(news_log)
    tree.write('news.xml')


if __name__ == "__main__":
    create_xml()