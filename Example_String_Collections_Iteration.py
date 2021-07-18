x ='qwe erty yuio pas dfgt lljkkl op'
data = x.encode('utf8')
print(data)
y=data.decode('utf8')
print(y==x)
print('='*50)
# List
List=["apple","orange","pear"]
print(List[1])
List[2]=8
print(List)
List_1 = []
List_1.append("Nhat")
List_1.append("Cuong")
print(List_1)
print(list("Vonhatcuong"))
print('='*50)
# Dirct
d = {'NhatCUong' :'0123', 'Bao':'456','Anh':'789'}
print(d)
print(d['NhatCUong'])
d['Anh']='0000'
print(d['Anh'])
d['xyz'] = '9999'
print(d)
print('='*50)
# For - Loop
for name in List:
    print(name)
print('\r')
for Name in d:
    print(Name,d[Name])
print('='*50)
#
from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)
print(story_words)
print('='*50)
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
print(story_words)