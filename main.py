from crawler import LinksCrawler


if __name__ == "__main__":

    ancher_text = 'laptop'
    link_crawl = LinksCrawler(ancher_text)
    data = link_crawl.find_data()
    print(len(data[0]))
    print(len(data[1]))

