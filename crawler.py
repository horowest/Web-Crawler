import urllib.request
import getlinks
import general_methods
import create_project

class Crawler:
    pname = ''
    base_url = ''
    queue = set()
    crawled = set()
    queue_file = ''
    crawled_file = ''


    def __init__(self, pname, base_url):
        Crawler.pname = pname
        Crawler.base_url = base_url
        Crawler.queue_file = pname + '/queue.txt'
        Crawler.crawled_file = pname + '/crawled.txt'
        self.boot()
        self.crawl(1, base_url)

    
    @staticmethod
    def boot():
        create_project.create_project(Crawler.pname, Crawler.base_url)
        Crawler.queue = general_methods.read_file(Crawler.queue_file)
        Crawler.crawled = general_methods.read_file(Crawler.crawled_file)
        #print(Crawler.queue, Crawler.crawled)

    
    @staticmethod
    def crawl(thread, page_url):
        #print("hey")
        if page_url not in Crawler.crawled:
            print("Crawling: ", page_url)
            link_set = Crawler.get_links(page_url)
            # updates
            Crawler.add_new_links(link_set)
            try:
                Crawler.queue.remove(page_url)
            except:
                print(page_url, "HOOO")    
            Crawler.crawled.add(page_url)
            Crawler.update_files()

    @staticmethod
    def get_links(page_url):
        try:
            #print("ran")
            r = urllib.request.urlopen(page_url)
            link_finder = getlinks.GetLinks()
            link_finder.feed(r.read().decode('utf-8'))
            link_set = link_finder.get_links()
            return link_set
        except:
            print("Cannot connect to ", page_url)
            return set()

    
    @staticmethod
    def add_new_links(link_set):
        for link in link_set:
            # print("ran")
            if link not in Crawler.queue and link not in Crawler.crawled and general_methods.same_site(Crawler.base_url, link):
                # print(link)
                Crawler.queue.add(link)

    
    @staticmethod
    def update_files():
        general_methods.write_file(Crawler.queue_file, Crawler.queue)
        general_methods.write_file(Crawler.crawled_file, Crawler.crawled)


# Crawler('sello', 'https://python.org')
# print(general_methods.read_file(Crawler.queue_file))
