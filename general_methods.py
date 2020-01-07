import urllib.parse
def get_domain(url):
    try:
        results = get_sub_domain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain(url):
    """ Get sub domain name (name.example.com)"""
    try:
        return urllib.parse.urlparse(url).netloc
    except:
        return ''


def same_site(base_url, page_url):
    """ check if the url is from the same base_url site"""
    if get_domain(base_url) == get_domain(page_url):
        return True
    return False


def read_file(fname):
    """ read a file and insert the items in a set() """
    link_set = set()
    # read links and add it link set
    with open(fname, 'r') as f:
        for line in f.readlines():
            link_set.add(line[:-1])    # [:-1] to remove '\n' in each line
    return link_set


def write_file(fname, link_set):
    """ write the links in the link_set in a file """
    with open(fname, 'w') as f:
        for link in link_set:
            f.write(link + '\n')


def append_file(fname, link_set):
    """ append the links in the link_set in a file """
    with open(fname, 'a') as f:
        for link in link_set:
            f.write(link + '\n')

# links = read_file('hello/queue.txt')
# write_file('hello/crawled.txt', links)    
# print(get_domain('https://www.mobi.debuggex.com/cheatsheet/regex/python'))
# f = open('python/crawled.txt')
# for line in f:
#     print(same_site('http://python.org', line), line, get_domain(line))
# f.close()