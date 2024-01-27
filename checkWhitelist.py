import csv
import requests
import re

def is_reachable(url):
    try:
        response = requests.get(url, timeout=10)
        # If the response status code is 200, the website is reachable
        if response.status_code == 200:
            print("Website is reachable: " + url)
            return "Reachable"
        else:
            print("Website is not reachable: " + url)
            return "Blocked"
    except requests.exceptions.RequestException as e:
        # If a request exception is raised, the website may be blocked
        print("Error: " + str(e))
        return("Error: " + str(e))

def expand_url(url):
    # List of known protocols
    # protocols = ['http://', 'https://', 'ftp://', 'sftp://', 'file://', 'mailto:', 'telnet://', 'ldap://', 'gopher://']
    # Remove each protocol from the URL
    # for protocol in protocols:
    #     url = url.replace(protocol, '')
    # Remove the last slash
    url = url.rstrip('/')
    # Remove wildcards
    url = url.replace('*.', '')
    # Remove whitespace
    url = url.replace(' ', '')
    # Check if the URL contains a pattern like [0–9]
    match = re.search(r'\[(\d)–(\d)\]', url)
    if match:
        start, end = map(int, match.groups())
        # Generate all possible URLs
        urls = [url[:match.start()] + str(i) + url[match.end():] for i in range(start, end+1)]
    else:
        urls = [url]
    # Add 'https://' to the start of the URL if it's not already present
    urls = ['https://' + url if not url.startswith('https://') else url for url in urls]
    return urls

with open('urls.csv', 'r') as file:
    reader = csv.reader(file)
    output_file = open('output.csv', 'w')
    writer = csv.writer(output_file)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        urls = expand_url(row[0])
        for url in urls:
            reachable = is_reachable(url)
            row[2] = reachable
        writer.writerow(row)
    output_file.close()
