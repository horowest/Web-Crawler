import urllib.request
import html.parser as hp
import pprint

class GetLinks(hp.HTMLParser):
    def __init__(self):
        super().__init__()
        self.link_set = set()

    def handle_starttag(self, tag, attrs):
        """ overrides HTMLParser method and gives page links"""
        if tag == 'a':      
            for (attr, value) in attrs:
                if attr == 'href':
                    if value[0] == 'h':
                        self.link_set.add(value)

    def get_links(self):
        """ returns the links found in the page"""
        return self.link_set


# links = GetLinks()
# links.feed('''<div class="dropdown-menu" aria-labelledby="more-langs">
# 		                <a class="dropdown-item" href="https://www.learnpython.org">Python</a>
# 		                <a class="dropdown-item" href="https://www.learnjavaonline.org">Java</a>
# 		                <a class="dropdown-item disabled" href="https://www.learn-html.org">HTML</a>
# 		                <a class="dropdown-item" href="https://www.learn-golang.org">Go</a>
# 		                <a class="dropdown-item" href="https://www.learn-c.org">C</a>
# 		                <a class="dropdown-item" href="https://www.learn-cpp.org">C++</a>
# 		                <a class="dropdown-item" href="https://www.learn-js.org">JavaScript</a>
# 		                <a class="dropdown-item" href="https://www.learn-php.org">PHP</a>
# 		                <a class="dropdown-item" href="https://www.learnshell.org">Shell</a>
# 		                <a class="dropdown-item" href="https://www.learncs.org">C#</a>
# 		                <a class="dropdown-item" href="https://www.learn-perl.org">Perl</a>
# 		                <a class="dropdown-item" href="https://www.learnrubyonline.org">Ruby</a>
# 		                <a class="dropdown-item" href="https://www.learnscala.org">Scala</a>
# 		                <a class="dropdown-item" href="https://www.learnsqlonline.org">SQL</a>
#                 </div>''')
#
# try:
#     r = urllib.request.urlopen('https://horowest.github.io')
#     links = GetLinks()
#     links.feed(r.read().decode('utf-8'))
#     print(links.get_links())
# except:
#     print("Cannot connect")