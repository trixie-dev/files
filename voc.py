# coding: utf8
import random
print('vocabulary v1.0')
print('Этапы действия, часть и целое - 1')
print('Движение - 2')
print('---------')
print('"Topic: " напиши номер теми')
print('"Method:" спосіб виконання. 1 англ-укр; 2 укр-англ')
print('Якщо правильно, натисни ентер, фкщо ні введи якийся символ')
t=True
#def js():

while True:
    k=int(input('Topic: '))
    q=int(input('Method: '))

    if k==1:
        l=[['become (became, become)', 'ставати'], ['begin (began, begun)', 'починати'], ['start', 'починати'], ['continue', 'продовжувати'], ['go on (went, gone)', 'продовжувати'], ['stop', 'закінчувати, зупиняти'], ['end', 'закінчувати'], ['finish', 'закінчувати'], ['last', 'тривати'], ['accomplish', 'завершувати'], ['prepare', 'готувати'], ['postpone', 'відкладати'], ['put off (put, put)', 'відкладати'], ['divide', 'розділяти'], ['consist of', 'складатися з'], ['include', 'включати (в себе щось)'], ['exclude', 'виключати'], ['incorporate', "включати (в себе щось), об'єднуватися"], ['split (split, split)', 'розділяти на частини, розщеплювати'], ['contain', 'містити в собі)'], ['separate', 'відокремлювати'], ['assemble', 'збирати (з частин)']]
    elif k==2:
        l=[['go (went, gone)', 'йти'], ['come (came, come)', 'приходити'], ['turn', 'повертати'], ['run (ran, run)', 'бігти'], ['move', 'рухати (-ся)'], ['bring (brought, brought)', 'приносити'], ['sit (sat, sat)', 'сидіти'], ['stand', 'стояти'], ['follow', 'дотримуватися'], ['stop', 'зупиняти (-ся)'], ['walk', 'ходити гуляти)'], ['appear', "з'являтися"], ['disappear', 'зникати'], ['remain', 'залишатися'], ['leave (left, left)', 'залишати'], ['raise', 'піднімати (-ся)'], ['carry', 'нести'], ['drive (drove, driven)', 'вести машину'], ['throw (threw, trown)', 'кидати'], ['push', 'штовхати'], ['lay (laid, laid)', 'класти'], ['lie (lay, lain)', 'лежати, брехати'], ['arrive', 'прибувати'], ['shake (shook, shaken)', 'трясти'], ['fly (flew, flown)', 'літати'], ['stay', 'залишатися'], ['fall (fell, fallen)', 'падати'], ['wear (wore, worn)', 'носити (напр', ' одяг)'], ['step', 'зробити крок'], ['roll', 'котитися, згортати'], ['ride (rode, ridden)', 'їхати (напр', ' верхом)'], ['lift', 'піднімати'], ['jump', 'стрибати'], ['approach', 'наближатися'], ['cross', 'перетинати'], ['climb', 'лізти (дертися)'], ['bear (bore, born)', 'нести'], ['shift', 'зрушувати'], ['slip', 'підсковзнутися'], ['rush', 'поспішати (стрімко мчати)'], ['land', 'приземлятися'], ['escape', 'втікати'], ['drag', 'тягти'], ['slide (slid, slid)', 'ковзати'], ['toss', 'кидати (метати)'], ['accompany', 'супроводжувати'], ['swing (swang, swung)', 'розгойдувати'], ['advance', 'просуватися'], ['swim (swam, swum)', 'плисти'], ['flee', 'тікати, рятуватися втечею'], ['sink (sank, sunk)', 'тонути']]
    elif k==3:
    	l=[['be (was, been)', 'бути'], ['exist', 'існувати'], ['include', 'включати (в себе що-небудь)'], ['exclude', 'виключати'], ['add', 'додавати'], ['enter', 'вводити, входити'], ['share', 'ділитися'], ['remove', 'видаляти'], ['receive', 'отримувати'], ['lose (lost, lost)', 'втрачати'], ['find (found, found)', 'знайти'], ['have (had, had)', 'мати'], ['be present', 'бути присутнім'], ['be absent', 'відсутні'], ['get (got, got\\gotten)', 'отримати (ставати)'], ['take (took, taken)', 'брати'], ['give (gave, given)', 'давати'], ['return', 'повертати'], ['join', 'приєднувати'], ['involve', 'залучати'], ['release', 'випускати (відпускати)'], ['own', 'володіти'], ['gain', 'отримувати, набирати (додавати в чомусь)'], ['emerge', "з'являтися"], ['expand', 'розширювати (-ся)'], ['disappear', 'зникати'], ['obtain', 'отримувати'], ['belong', 'належати'], ['limit', 'обмежувати'], ['spread (spread, spread)', 'поширювати (-ся)'], ['extend', 'розширювати (-ся)'], ['acquire', 'здобувати (отримувати)'], ['abandon', 'залишати'], ['arise (arose, arisen)', 'виникати'], ['possess', 'володіти (володіти)'], ['leave (left, left)', 'залишити'], ['occupy', 'займати місце)']]
    full=len(l)
    add=0
    u=0
    u=1
    prav = 0
    if q==1:
        while len(l)!=0:
            print(u)
            u+=1
            i=random.randint(0, len(l)-1)
            print(l[i][0])
            o=input(': ')
            print(l[i][1])
            r=str(input())
            if r=='':
                l.remove(l[i])
                prav+=1
            elif r=='0':
                t=False
            else:
            	add+=1
            print('---------------')
    else:
        while len(l)!=0:
            print(u)
            u+=1
            i=random.randint(0, len(l)-1)
            print(l[i][1])
            o=input(': ')
            print(l[i][0])
            r=str(input())
            if r=='':
                l.remove(l[i])
                prav+=1
            elif r=='0':
                t=False
            else:
            	add+=1
            print('---------------')
    res = (100*prav)/(full+add)
    print(int(res), "%")
