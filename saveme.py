#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import json
import math
import os

'''
This tool's settings
'''

ORIGIN_MOOD_FILE_PATH = "/Users/shanhaoqi/MyLove/niklaus520.github.com/source/life_origin/life.json"
HEXO_COMMAND_PATH = ""
ALL_TITLE = '''
title: Title does not matter, life does matter
---

<blockquote class="blockquote-center">应该算是生活.
不用⌘ + R</blockquote>

'''
PAGINATION_BASE = "/life"
SOURSE_DIR_BASE = "/Users/shanhaoqi/MyLove/niklaus520.github.com/source"
'''
Generate the pagination html code for specified page number
'''


def UrlFormat(page_number):
    global PAGINATION_BASE
    if PAGINATION_BASE[len(PAGINATION_BASE) - 1] is not '/':
        PAGINATION_BASE += '/'
    if page_number is 1:
        return ('''<a class="page-number" href="''' + \
            PAGINATION_BASE + \
            '''">1</a>'''
        )
    else:
        return ('''<a class="page-number" href="''' + \
            PAGINATION_BASE + \
            str(page_number) + \
            '.html' + \
            '''">''' + \
            str(page_number) + \
            '''</a>''')


def GeneratePrevPage(current_page_number):
    global PAGINATION_BASE
    if PAGINATION_BASE[len(PAGINATION_BASE) - 1] is not '/':
        PAGINATION_BASE += '/'
    if current_page_number - 1 is 1:
        return ('''<a class="extend prev" rel="prev" href="''' + \
            PAGINATION_BASE + \
            '''">&laquo;</a>'''
        )
    else:
        return ('''<a class="extend prev" rel="prev" href="''' + \
    PAGINATION_BASE + \
    str(current_page_number - 1) + \
    '.html' + \
    '''">&laquo;</a>''')


def GenerateNextPage(current_page_number):
    global PAGINATION_BASE
    if PAGINATION_BASE[len(PAGINATION_BASE) - 1] is not '/':
        PAGINATION_BASE += '/'
    return ('''<a class="extend next" rel="next" href="''' + \
    PAGINATION_BASE + \
    str(current_page_number + 1) + \
    '.html' + \
    '''">&raquo;</a>''')


def GeneratePagination(current_page_number, total_page_number, each_side_number = 1):
    global PAGINATION_BASE
    if PAGINATION_BASE[len(PAGINATION_BASE) - 1] is not '/':
        PAGINATION_BASE += '/'
    PaginationHtmlCode = '''<div class="pagination">'''
    DebugOutput = ' '
    if current_page_number > 1:
        PaginationHtmlCode += GeneratePrevPage(current_page_number)
        DebugOutput += ''' << '''
    if total_page_number <= (2 * each_side_number) + 5:
        start_page_number = 1
        end_page_number = total_page_number
    elif current_page_number <= each_side_number + 1:
        start_page_number = 1
        end_page_number = each_side_number + 2
    elif current_page_number >= total_page_number - (each_side_number + 1):
        start_page_number = total_page_number - (each_side_number + 2)
        end_page_number = total_page_number
    else:
        start_page_number = current_page_number - each_side_number
        end_page_number = current_page_number + each_side_number
    if start_page_number > 1:
        DebugOutput += ' 1 '
        PaginationHtmlCode += UrlFormat(1)
    if start_page_number > 2:
        DebugOutput += ' ... '
        PaginationHtmlCode += '''<span class="space">&hellip;</span>'''
    for page_number in range(start_page_number, end_page_number + 1):
        DebugOutput += ' '
        DebugOutput += str(page_number)
        DebugOutput += ' '
        if page_number is not current_page_number:
            PaginationHtmlCode += UrlFormat(page_number)
        else:
            PaginationHtmlCode += '''<span class="page-number current">'''
            PaginationHtmlCode += str(page_number)
            PaginationHtmlCode += '''</span>'''
    if end_page_number < total_page_number - 1:
        DebugOutput += ''' ... '''
        PaginationHtmlCode += '''<span class="space">&hellip;</span>'''
    if end_page_number < total_page_number:
        DebugOutput += str(total_page_number)
        PaginationHtmlCode += UrlFormat(total_page_number)
    if current_page_number is not total_page_number:
        PaginationHtmlCode += GenerateNextPage(current_page_number)
        DebugOutput += ''' >> '''
    print DebugOutput
    PaginationHtmlCode += '''</div>''' 
    return PaginationHtmlCode


def GeneratePageContent(page_number, total_page_number, content = 'test content'):
    # Check if there is same page existed already
    global PAGINATION_BASE, SOURSE_DIR_BASE
    if PAGINATION_BASE[len(PAGINATION_BASE) - 1] is not '/':
        PAGINATION_BASE += '/'
    if page_number is 1:
        page_path = SOURSE_DIR_BASE + PAGINATION_BASE + 'index.md'
    else:
        page_path = SOURSE_DIR_BASE + PAGINATION_BASE + str(page_number) + '.md'
    if os.path.isfile(page_path):
        os.remove(page_path)
    page_file = open(page_path, 'a')
    page_file.write(ALL_TITLE)
    page_file.write('\n')
    page_file.write(content)
    page_file.write('\n')
    page_file.write(GeneratePagination(page_number, total_page_number))
    page_file.write('\n')
    page_file.close()


def ReadAndWriteMood(mood_file_path):
    with open(mood_file_path) as data:
        moods = json.load(data)
    if len(moods['life']) == 0:
        return
    if len(moods['life']) <= 10:
        total_page_number = 1
    else:
        total_page_number = math.trunc(math.ceil((len(moods['life']) - 10) / 9) + 1)
        # print "total moods length: " + str(len(moods['life']))
        # print "total_page_number: " + str(total_page_number)
    moods_in_page = ''' '''
    #for i in range(0, len(moods['life']) if total_page_number == 1 else 10):
    #    moods_in_page += '\r\n\r\n'
    #    moods_in_page += moods['life'][i]['created_at'].encode("utf-8")
    #    moods_in_page += '\r\n\r\n'
    #    moods_in_page += moods['life'][i]['content'].encode("utf-8")
    #    moods_in_page += '\r\n\r\n'
    #    moods_in_page += '''---'''
    #GeneratePageContent(1, total_page_number, moods_in_page)
    #if total_page_number > 1:
    for i in range(0, total_page_number):
        for j in range(1 + 9 * i, 11 + 9 * i if (11 + 9 * i) <= (len(moods['life']) + 1 ) else len(moods['life']) + 1):
            # print str(j)
            moods_in_page += '\r\n\r\n'
            moods_in_page += moods['life'][j - 1]['created_at'].encode("utf-8")
            moods_in_page += '\r\n\r\n'
            moods_in_page += moods['life'][j - 1]['content'].encode("utf-8")
            moods_in_page += '\r\n\r\n'
            moods_in_page += '''---'''
        GeneratePageContent(i + 1, total_page_number, moods_in_page)

if __name__ == '__main__':
    #print GeneratePagination(2, 3, 1)
    #for page_number in range(1, 16):
    #    GeneratePageContent(page_number, 15, 'test content, page ' + str(page_number))
    #global ORIGIN_MOOD_FILE_PATH
    ReadAndWriteMood(ORIGIN_MOOD_FILE_PATH)