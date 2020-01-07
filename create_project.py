import os

def create_files(pname, base_url):
    """ creates queue.txt & crawled.txt """
    queue_file = pname + "/queue.txt"
    crawled_file = pname + "/crawled.txt"

    # create queue.txt
    if not os.path.exists(queue_file):
        f = open(queue_file, 'w')
        f.write(base_url)
        print(base_url)
        f.close

    # create crawled.txt
    if not os.path.exists(crawled_file):
        with open(crawled_file, 'w'):
            pass


def create_project(pname, base_url):
    """ create a new project dir """
    if not os.path.exists(pname):
        os.mkdir(pname)
    create_files(pname, base_url)

# create_project('hello', 'hello.com')