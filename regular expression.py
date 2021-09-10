#1
import re
def text_match(text):
    patterns='a*b$'
    if re.search(patterns,text):
        return 'found'
    else:
        return 'not found'
print(text_match("babbloo"))
print(text_match("abcg"))
print(text_match("abbbb"))


#2
import re
def text(text):
    patterns='\Ahai'
    if re.search(patterns,text):
        return 'found'
    else:
        return 'not found'
print(text("hai my name is Ansheena"))
print(text("hello my name is Ansheena"))

#3
import re
def text(text):
    patterns='^5'
    if re.search(patterns,text):
        return 'found'
    else:
        return 'not found'
print(text("AN5HI"))
print(text("5ANSHI"))

#4
import re
def text1(text):
    pattern = 'LOVE'
    if re.findall(pattern,text):
        return 'found'
    else:
        return 'not found'
print(text1("i LOVE india"))
print(text("india is my country"))

#5
import re
text = 'hello world'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)

#6
import re
txt="1b2c3d4e5f6"
x=re.split("\D+",txt)
print(x)

    
    
