import general_methods
import crawler


# test project
PROJECT_NAME = 'python'
HOMEPAGE = 'http://python.org/'
DOMAIN_NAME = general_methods.get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
crawler.Crawler(PROJECT_NAME, HOMEPAGE)


def work():
    """Each queued link is a new job"""
    for url in general_methods.read_file(QUEUE_FILE):
        crawler.Crawler.crawl(1, url)
    crawl()


def crawl():
    """Check if there are items in the queue, if so crawl them"""
    queued_links = general_methods.read_file(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        work()

def main():
    crawl()

if __name__ == "__main__":
    main()
