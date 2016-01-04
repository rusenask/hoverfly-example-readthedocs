#!/usr/bin/env python
from argparse import ArgumentParser

import requests
import pickle
from tqdm import tqdm

limit = 50


# getting urls and dumping them into file
def get_urls():
    sites = requests.get("http://readthedocs.org/api/v1/project/?limit=%s&offset=0" % limit)

    objects = sites.json()['objects']

    links = [x['subdomain'] for x in objects]

    with open("links.p", "wb") as outfile:
        pickle.dump(links, outfile)


def add_iterations(links, iterations):
    if not iterations:
        return links

    new_links = []

    for _ in range(iterations):
        new_links.extend(links)

    print("Set to %s iterations, total links: %s" % (iterations, len(new_links)))
    return new_links


def fetch_links(iterations):
    with open("links.p", "rb") as infile:
        links = pickle.load(infile)

    links = add_iterations(links, iterations)

    import time
    start = time.time()

    pbar = tqdm(links)
    for link in pbar:
        response = requests.get(link)
        pbar.set_description("Processing links.. (status %s)" %  response.status_code)
        # do something more with it?
        # print("url: %s, status code: %s" % (link, response.status_code))

    print("Time taken: %s" % (time.time() - start))


# main function
def main():
    parser = ArgumentParser(description="Perform proxy testing/URL list creation")
    parser.add_argument("--urls", help="download and save urls ('./fetch.py --urls 1') ")
    parser.add_argument("--iterations", help="number of iterations")

    args = parser.parse_args()

    # get urls
    if args.urls:
        get_urls()
    else:
        fetch_links(int(args.iterations))


if __name__ == "__main__":
    main()
