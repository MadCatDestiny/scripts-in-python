"""
Меняет текст в буфере обмена,меняя раскладку для латинских букв =)
"""
import pyperclip
import keyboard

def change():
    spam = pyperclip.paste()
    spam = list(spam)
    res = ''
    chars = {'q':'й','w':'ц','e':'у','r':'к','t':'е','y':'н','u':'г','i':'ш','o':'щ','p':'з','[':'х',']':'ъ','a':'ф','s':'ы',
             'd':'в','f':'а','g':'п','h':'р','j':'о','k':'л','l':'д',';':'ж','\'':'э','z':'я','x':'ч','c':'с','v':'м','b':'и',
             'n':'т','m':'ь',',':'б','.':'ю','/':'.','@':'"','#':'№','$':';','%':'%','^':':','&':'?','Q':'Й','W':'Ц','E':'У',
             'R':'К','T':'Е','Y':'Н','U':'Г','I':'Ш','O':'Щ','P':'З','{':'Х','}':'Ъ','A':'Ф','S':'Ы','D':'В','F':'А','G':'П',
             'H':'Р','J':'О','K':'Л','L':'Д',':':'Ж','"':'Э','Z':'Я','X':'Ч','C':'С','V':'М','B':'И','N':'Т','M':'Ь','<':'Б',
             '>':'Ю','?':','}

    rchars = dict.fromkeys(chars.values())
    for k,v in chars.items():
        rchars[v] = k

    if spam[0] in chars.keys():
        for i in spam:
            try:
                res+=chars[i]
            except KeyError:
                res += i
    else:
        for i in spam:
            try:
                res+=rchars[i]
            except KeyError:
                res += i
    pyperclip.copy(res)
    """
    for i in spam:
        try:
            if i in chars.keys():
                res+=chars[i]
            elif i in rchars.keys():
                res+=rchars[i]
            else:
                res += i
        except KeyError:
            res += i
    """
    #print('res: ' + res)
    #print(len(spam) == len(res))
    #qwertyuiop[asdfghjkl;'zxcvbnm,./!@#$%^&*()_+1234567890-=QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?йцу


keyboard.add_hotkey('Ctrl + Shift + .',change)
keyboard.wait()
