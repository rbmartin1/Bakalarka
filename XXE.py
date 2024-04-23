from lxml import etree

def parse_xml(xml_data):
    # Parse the XML data
    try:
        # Vytvorenie parsera s vypnutým rozširovaním entít a bez prístupu k sieti
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_data, parser)
        # Extract informácií z XML
        username = root.find('username').text
        password = root.find('password').text
        return f'Username: {username}, Password: {password}'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    # XML data obsahujuce prihlasovacie udaje
    xml_data = """
    <!DOCTYPE data [
        <!ENTITY xxe SYSTEM "file:///etc/passwd">
    ]>
    <data>
        <username>admin</username>
        <password>&xxe;</password>
    </data>
    """
    
    # prevolanie funckie
    result = parse_xml(xml_data)
    print(result)











