from json import load

with open('idiom.json', 'r') as file:
    idioms = [idiom for idiom in load(file) ]

if __name__ == '__main__':
    print(idioms)