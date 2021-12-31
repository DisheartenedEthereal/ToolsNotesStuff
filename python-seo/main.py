from googlesearch import search
import os
from bs4 import BeautifulSoup
import requests


def get_results(query):
    google_results = [j for j in search(query, num=10, stop=10, pause=2)]
    return google_results


def make_files(name):
    os.mkdir("/home/ethereal/seo/"+name)
    path = "/home/ethereal/seo/" + name
    return path


def write_results(list_of_results, path):
    f = open(path + "links.txt")
    f.write(list_of_results)
    f.close()


def extract_meta(url):
    URLS = ['http://www.astro.com',
            'http://www.supermap.com',
            'http://www.itc.com']
    ATTRIBUTES = ['description', 'keywords', 'Description', 'Keywords']

    collected_data = []

    for url in URLS:
        entry = {'url': url}
        try:
            r = requests.get(url)
        except Exception as e:
            print('Could not load page {}. Reason: {}'.format(url, str(e)))
            continue
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            meta_list = soup.find_all("meta")
            for meta in meta_list:
                if 'name' in meta.attrs:
                    name = meta.attrs['name']
                    if name in ATTRIBUTES:
                        entry[name.lower()] = meta.attrs['content']
            if len(entry) == 3:
                collected_data.append(entry)
            else:
                print('Could not find all required attributes for URL {}'.format(url))
        else:
            print('Could not load page {}.Reason: {}'.format(url, r.status_code))
    print('Collected meta attributes (TODO - push to file):')
    return collected_data
