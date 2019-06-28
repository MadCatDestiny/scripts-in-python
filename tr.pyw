
import pyperclip
spam = pyperclip.paste()
#print(spam)
spam = list(spam)
res = ''
chars = {'q':'й','w':'ц','e':'у','r':'к','t':'е','y':'н','u':'г','i':'ш','o':'щ','p':'з','[':'х',']':'ъ','a':'ф','s':'ы','d':'в','f':'а','g':'п','h':'р','j':'о','k':'л','l':'д',';':'ж','\'':'э','z':'я','x':'ч','c':'с','v':'м','b':'и','n':'т','m':'ь',',':'б','.':'ю','/':'.','@':'"','#':'№','$':';','%':'%','^':':','&':'?'}
for i in spam:
    try:
        res+=chars[i]
    except KeyError:
        #print('ERR:'+ i )
        res += i
        pass
    except TypeError:
        pass
#print(res)
#print(len(spam) == len(res))
pyperclip.copy(res)