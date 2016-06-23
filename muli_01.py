import multiprocessing
import Queue
import urllib2


NUM_PROCESS = 2
NUM_URL = 1000


class DownloadProcess(multiprocessing.Process):
    """Download Process """

    def __init__(self, urls_queue, result_queue):

        multiprocessing.Process.__init__(self)

        self.urls = urls_queue
        self.result = result_queue

    def run(self):
        while True:

             try:
                 url = self.urls.get_nowait()
             except Queue.Empty:
                 break

             ret = urllib2.Request(url)
             res = urllib2.urlopen(ret)

             try:
                 result = res.read()
             except (urllib2.HTTPError, urllib2.URLError):
                     pass

             self.result.put(result)


def main():

    main_url = 'http://server/?%s'

    urls_queue = multiprocessing.Queue()
    for p in range(1, NUM_URL):
        urls_queue.put(main_url % p)

    result_queue = multiprocessing.Queue()

    for i in range(NUM_PROCESS):
        download = DownloadProcess(urls_queue, result_queue)
        download.start()

    results = []
    while result_queue:
        result = result_queue.get()
        results.append(result)

    return results

if __name__ == "__main__":
    results = main()

    for res in results:
        print(res)