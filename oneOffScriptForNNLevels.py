import re


globalJSON = ""

def newStr(text):
    match = re.search(r'\bvar\s+(\w+)\s+=', text)
    if match:
        result = match.group(1)
        return text[:-5] + 'I18n_HAIW23L3.translate("' + result + '")};'
    else:
        return text

def jsonObj(text):
    global globalJSON
    match = re.search(r'\bvar\s+(\w+)\s+=', text)
    if not match and text != "":
        globalJSON = text[2:-1]
        return
    if match:
        result = match.group(1)
        return 'translatedObject[' + globalJSON + '.i18n][' + result + '.i18n] = recommendationObject[' + globalJSON + '.en][' + result + '.en];'

# this function takes in a file of strings and, for each line in the file, calls newStr() to replace the string with the translated string  
def translateFile(file):
    with open(file, 'r', errors='replace') as f:
        for line in f:
            print(newStr(line))

def buildJson(file):
    with open(file, 'r', errors='replace') as f:
        for line in f:
            print(jsonObj(line))

translateFile('strings.txt')
buildJson('strings.txt')