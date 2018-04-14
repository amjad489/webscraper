def get_versions(url, xpath):
    """
    parse the page and finds the version
    :param url:
    :param xpath:
    :return:
    """
    page_version = ""
    try:
        print("fetching content for {0}".format(url))
        page = requests.get(url)
        logging.debug(page.content)
        page_tree = html.fromstring(page.content)
        page_version = page_tree.xpath(xpath)
        page_version = re.findall(r'(\d+\.\d+\.\d+\.\d+-.*|\d+\.\d+\.\d+)', page_version[0])  # fetch only version
        print("page version is {0}".format(page_version))
    except IndexError as IE:
        print("{0} - unable to fetch version, url {1}, xpath {2}, page_content {3}".
                      format(IE.message, url, xpath, page_version), exc_info=True)
