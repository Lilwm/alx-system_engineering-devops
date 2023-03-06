#!/usr/bin/python3
"""
1-main
"""
import sys


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv)< 2:
        print("please pass an argument for the subreddit")
    else:
        top_ten(sys.argv[1])
