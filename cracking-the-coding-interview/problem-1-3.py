# URL generator, take string and replaces spaces for %20

def URLify(string):
    output = ""
    i = 0
    while i < len(string):
        if string[i] != " ":
            output += string[i]
            i += 1
        elif string[i] == " ":
            while string[i] == " ":
                i += 1
            output += "%20"

    return output

strings = ['Barry Manilow', 'Jadon Sancho', 'Jonny  Two  Space',
           'JonnyNoSpace']

for i in strings:
    print(URLify(i))
