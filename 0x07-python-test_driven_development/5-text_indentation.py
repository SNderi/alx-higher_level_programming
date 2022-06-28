#!/usr/bin/python3
'''Module to print a text with 2 new lines after
each of these characters: ., ? and :
'''


def text_indentation(text):
    '''Adds two new lines after ., ? and :

    Args:
        text (str): String to print

    Raises:
        TypeError: if text is not a string
    '''
    triggers = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for tracker in range(len(text)):
        if text[tracker] == ' ' and tracker == 0:
            tracker += 1
            continue
        if text[tracker] == ' ' and (text[tracker - 1] in triggers or text[tracker -1] == ' '):
            tracker += 1
            continue
        if text[tracker] in triggers:
            print(text[tracker], end='\n')
            print()
        else:
            print(text[tracker], end='')
