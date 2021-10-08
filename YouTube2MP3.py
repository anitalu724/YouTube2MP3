
import argparse
import sys, os
from download import *

def main():
    parser = argparse.ArgumentParser(description='YouTube2MP3', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-u', '--url', help='The URL of the youtube video.\n')
    parser.add_argument('-f', '--file', help='The TSV file for all URLs and names.\n')
    parser.add_argument('-n', '--name', help='The name of the downloaded file.\n')
    parser.add_argument('-p', '--position', help='The position of downloading.\n')

    args = parser.parse_args()
    
    if args.url == None and args.file == None:
        raise ValueError('[YouTube2MP3] Command -u and -f need to choose one to use.')
    
    url_list, name_list = [], []
    if args.url != None and args.file == None:
        url_list.append(url_list)
        if args.name != None:
            name_list.append(args.name)
        else:
            name_list.append('_')
    elif args.url == None and args.file != None:
        url_list, name_list = readFile(args.file)

    if args.position == None:
        download(url_list, name_list)
    else:
        download(url_list, name_list, args.position)


if __name__ == '__main__':
    main()

