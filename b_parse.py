from datetime import datetime
import b_sentence_fr

def nostop(val):
    return val not in b_sentence_fr.byebye

def inTheString(_lst, _str):
    for item in _lst:
        if item in _str:
            return True
    return False

def parse_sentect(val):
    if inTheString(b_sentence_fr.time, val):
        return datetime.now().strftime("%H:%M:%S")
    if (b_sentence_fr.date in val):
        return datetime.now().strftime("%A %d %B, %Y")
    return val