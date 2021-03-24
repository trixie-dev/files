# coding: utf8
import random
from termcolor import *
import colorama
colorama.init()
cprint('vocabulary v1.2', 'blue')
print("Виберіть пункт")
print(' ')
print('1 - Дієслова')
print('2 - Іменник')
print('3 - Прикметник')
print('4 - Прислівник')
print('5 - Прийменники')
print('6 - Сполучники')
print('7 - Всі слова')
print('8 - Інструкція')
var=int(input(': '))

if var == 1:
    print('1  - Этапы действия, часть и целое')
    print('2  - Движение')
    print('3  - Наличие\отсутствие, принадлежность')
    print('4  - Работа, сотрудничество')
    print('5  - Чувства')
    print('6  - Общение')
    print('7  - Борьба')
    print('8  - Экономика')
    print('9  - Человек')
    print('10 - Дом, быт, развлечение')
    print('11 - Физическое действие(общие)')
    print('12 - Закон')
    print('13 - Физическое действие(человека)')
elif var == 8:
    cprint('"Topic: " напиши номер теми', attrs=['reverse'])
    cprint('"Method:" спосіб виконання. 1 англ-укр; 2 укр-англ', attrs=['reverse'])
    cprint('Якщо правильно, натисни ентер, якщо ні введи якийся символ', attrs=['reverse'])
t=True
#def js():

while True:
    k=int(input('Topic: '))
    q=int(input('Method: '))
    if k == 0:
        break
    elif k==1:
        l=[['become (became, become)', 'ставати'], ['begin (began, begun)', 'починати'], ['start', 'починати'], ['continue', 'продовжувати'], ['go on (went, gone)', 'продовжувати'], ['stop', 'закінчувати, зупиняти'], ['end', 'закінчувати'], ['finish', 'закінчувати'], ['last', 'тривати'], ['accomplish', 'завершувати'], ['prepare', 'готувати'], ['postpone', 'відкладати'], ['put off (put, put)', 'відкладати'], ['divide', 'розділяти'], ['consist of', 'складатися з'], ['include', 'включати (в себе щось)'], ['exclude', 'виключати'], ['incorporate', "включати (в себе щось), об'єднуватися"], ['split (split, split)', 'розділяти на частини, розщеплювати'], ['contain', 'містити в собі)'], ['separate', 'відокремлювати'], ['assemble', 'збирати (з частин)']]
    elif k==2:
        l=[['go (went, gone)', 'йти'], ['come (came, come)', 'приходити'], ['turn', 'повертати'], ['run (ran, run)', 'бігти'], ['move', 'рухати (-ся)'], ['bring (brought, brought)', 'приносити'], ['sit (sat, sat)', 'сидіти'], ['stand', 'стояти'], ['follow', 'дотримуватися'], ['stop', 'зупиняти (-ся)'], ['walk', 'ходити гуляти)'], ['appear', "з'являтися"], ['disappear', 'зникати'], ['remain', 'залишатися'], ['leave (left, left)', 'залишати'], ['raise', 'піднімати (-ся)'], ['carry', 'нести'], ['drive (drove, driven)', 'вести машину'], ['throw (threw, trown)', 'кидати'], ['push', 'штовхати'], ['lay (laid, laid)', 'класти'], ['lie (lay, lain)', 'лежати, брехати'], ['arrive', 'прибувати'], ['shake (shook, shaken)', 'трясти'], ['fly (flew, flown)', 'літати'], ['stay', 'залишатися'], ['fall (fell, fallen)', 'падати'], ['wear (wore, worn)', 'носити (напр', ' одяг)'], ['step', 'зробити крок'], ['roll', 'котитися, згортати'], ['ride (rode, ridden)', 'їхати (напр', ' верхом)'], ['lift', 'піднімати'], ['jump', 'стрибати'], ['approach', 'наближатися'], ['cross', 'перетинати'], ['climb', 'лізти (дертися)'], ['bear (bore, born)', 'нести'], ['shift', 'зрушувати'], ['slip', 'підсковзнутися'], ['rush', 'поспішати (стрімко мчати)'], ['land', 'приземлятися'], ['escape', 'втікати'], ['drag', 'тягти'], ['slide (slid, slid)', 'ковзати'], ['toss', 'кидати (метати)'], ['accompany', 'супроводжувати'], ['swing (swang, swung)', 'розгойдувати'], ['advance', 'просуватися'], ['swim (swam, swum)', 'плисти'], ['flee', 'тікати, рятуватися втечею'], ['sink (sank, sunk)', 'тонути']]
    elif k==3:
    	l=[['be (was, been)', 'бути'], ['exist', 'існувати'], ['include', 'включати (в себе що-небудь)'], ['exclude', 'виключати'], ['add', 'додавати'], ['enter', 'вводити, входити'], ['share', 'ділитися'], ['remove', 'видаляти'], ['receive', 'отримувати'], ['lose (lost, lost)', 'втрачати'], ['find (found, found)', 'знайти'], ['have (had, had)', 'мати'], ['be present', 'бути присутнім'], ['be absent', 'відсутні'], ['get (got, got\\gotten)', 'отримати (ставати)'], ['take (took, taken)', 'брати'], ['give (gave, given)', 'давати'], ['return', 'повертати'], ['join', 'приєднувати'], ['involve', 'залучати'], ['release', 'випускати (відпускати)'], ['own', 'володіти'], ['gain', 'отримувати, набирати (додавати в чомусь)'], ['emerge', "з'являтися"], ['expand', 'розширювати (-ся)'], ['disappear', 'зникати'], ['obtain', 'отримувати'], ['belong', 'належати'], ['limit', 'обмежувати'], ['spread (spread, spread)', 'поширювати (-ся)'], ['extend', 'розширювати (-ся)'], ['acquire', 'здобувати (отримувати)'], ['abandon', 'залишати'], ['arise (arose, arisen)', 'виникати'], ['possess', 'володіти (володіти)'], ['leave (left, left)', 'залишити'], ['occupy', 'займати місце)']]
    elif k == 4:
        l=[['work', 'працювати'], ['keep (kept, kept)', 'зберігати'], ['help', 'допомагати'], ['write (wrote, written)', 'писати'], ['provide', 'забезпечувати'], ['pay (paid, paid)', 'платити'], ['lead (led, led)', 'лідирувати (очолювати)'], ['create', 'створювати'], ['serve', 'служити'], ['build (built, built)', 'будувати'], ['develop', 'розвивати (розробляти)'], ['base', 'базувати, розміщувати'], ['realize', 'реалізувати, усвідомлювати'], ['save', 'зберігати (робити заощадження)'], ['fail', 'терпіти невдачу'], ['check', 'перевіряти'], ['design', 'розробляти'], ['claim', "пред'являти претензії, заявляти про права, стверджувати"], ['establish', 'встановлювати'], ['maintain', 'підтримувати'], ['head', 'керувати (очолювати)'], ['control', 'контролювати'], ['apply', 'подавати заяву, застосовувати щось'], ['manage', 'керувати'], ['perform', 'виконувати'], ['improve', 'поліпшувати'], ['sign', 'підписувати'], ['test', 'перевіряти (тестувати)'], ['prevent', 'запобігати'], ['publish', 'публікувати'], ['achieve', 'досягати (домагатися чогось)'], ['conduct', 'проводити'], ['attend', 'брати участь, відвідувати'], ['complete', 'виконувати'], ['handle (Handle with care)', 'звертатися (працювати з будь-чим, звич', ' вручну)'], ['handle (I can handle it)', 'справлятися (напр', ' з проблемою)'], ['deliver', 'доставляти'], ['operate', 'управляти (зазвичай механізмом, машиною, програмою)'], ['order', 'наказувати, замовляти'], ['measure', 'вимірювати'], ['engage', 'входити в контакт (займатися)'], ['hire', 'наймати на роботу'], ['train', 'навчати'], ['paint', 'фарбувати'], ['direct', 'керувати (управляти)'], ['solve', 'вирішувати (проблему, задачу)'], ['file', 'вносити в запису'], ['employ', 'приймати на роботу'], ['make (made, made)', 'робити, змушувати'], ['try', 'пробувати, намагатися'], ['happen', 'траплятися'], ['set (set, set)', 'встановлювати'], ['seek', 'Шукати'], ['fill', 'заповнювати'], ['pass', 'проходити, передавати'], ['attempt', 'намагатися'], ['connect', "підключати (з'єднувати)"], ['record', 'записувати'], ['locate', "виявити (з'ясувати місце розташування)"], ['search', 'шукати, обшукувати'], ['select', 'вибирати'], ['launch', 'запускати'], ['adjust', 'налаштовувати'], ['succeed', 'досягати мети (процвітати у чомусь)'], ['review', 'переглядати, робити огляд'], ['arrange (an event)', 'організовувати (захід)'], ['benefit', 'отримувати вигоду'], ['coach', 'тренувати'], ['exercise', 'вправлятися'], ['monitor', 'спостерігати'], ['supply', 'забезпечувати'], ['assist', 'допомагати'], ['construct', 'будувати'], ['schedule', 'складати графік, вносити в графік'], ['assign', 'призначати, давати завдання'], ['dismiss', 'звільняти'], ['practice', 'практикуватися'], ['illustrate', 'ілюструвати'], ['enhance', 'покращувати, посилювати'], ['implement', 'виконувати, застосовувати'], ['preserve', 'зберігати (уберігати)'], ['guide', 'вести (надсилати)'], ['illustrate', 'ілюструвати'], ['deserve', 'заслуговувати чогось'], ['face (something)', 'зустрітися з чимось (напр', ' з проблемою)'], ['cause', 'заподіювати що-небудь']]
    elif k == 5:
        l=[['teach (taught, taught)', 'вчити (навчати)'], ['can (could) ', 'могти, бути здатним'], ['know (knew, known)', 'знати'], ['think (thought, thought)', 'думати'], ['see (saw, seen)', 'бачити'], ['want', 'хотіти'], ['look', 'дивитися, виглядати'], ['need', 'потребувати'], ['feel (felt, felt)', 'відчувати'], ['mean (meant, meant)', 'значити (мати на увазі)'], ['seem', 'здаватися'], ['hear (heard, heard)', 'чути'], ['like', 'подобатися (любити)'], ['believe', 'вірити'], ['learn (learnt, learnt)', 'вивчати'], ['watch', 'дивитися (вартувати)'], ['read (read, read)', 'читати'], ['remember', "пам'ятати"], ['love', 'кохати'], ['decide', 'вирішувати'], ['hope', 'сподіватися'], ['listen', 'слухати'], ['focus', 'зосереджуватися (на чому-небудь)'], ['plan', 'планувати'], ['note', 'помічати, звертати увагу'], ['identify', 'ідентифікувати'], ['determine', 'визначати'], ['recognize', 'дізнаватися'], ['compare', 'порівнювати'], ['miss (someone)', 'нудьгувати (по кому-то \\ чогось)'], ['study', 'вивчати (вчитися)'], ['forget (forgot, forgotten)', 'забувати'], ['imagine', 'уявляти'], ['discover', 'здійснювати відкриття'], ['worry', 'турбуватися'], ['wait', 'чекати'], ['experience', 'переживати (відчувати щось на собі)'], ['tend', 'мати схильність (до чогось)'], ['notice', 'помічати'], ['wish', 'бажати'], ['figure out', "з'ясовувати (знаходити рішення)"], ['suffer', 'страждати'], ['recall', 'згадувати'], ['stare', 'пильно дивитися, витріщатися'], ['examine', 'перевіряти (вивчати)'], ['define', 'визначати'], ['observe', 'спостерігати'], ['count', 'вважати'], ['associate', 'асоціювати (з чимось)'], ['view', 'дивитися'], ['remind', 'нагадувати'], ['hate', 'ненавидіти'], ['intend', 'мати намір'], ['explore', 'досліджувати'], ['predict', 'передбачати'], ['acknowledge', 'визнавати, підтверджувати отримання'], ['fear', 'боятися'], ['conclude', 'робити висновок'], ['prefer', 'надавати перевагу'], ['appreciate', 'цінувати'], ['trust', 'довіряти'], ['rely on', 'покладатися на'], ['question', 'брати під сумнів, допитувати'], ['regard', 'враховувати, вважати ким-небудь \\ чим-небудь'], ['suspect', 'підозрювати'], ['suppose', 'припускати'], ['perceive', 'сприймати'], ['inspire', 'надихати'], ['analyze', 'аналізувати'], ['concentrate', 'зосереджуватися'], ['smell (smelt, smelt)', 'нюхати, пахнути'], ['glance', 'дивитися (кидати погляд)'], ['dream (dreamt, dreamt)', 'мріяти (бачити сни)'], ['react', 'реагувати'], ['choose', 'вибирати'], ['expect', 'очікувати'], ['miss', 'упускати, нудьгувати'], ['realize', 'реалізувати, усвідомлювати']]
    elif k == 6:
        l=[['say (said, said)', 'сказати'], ['tell (told, told)', 'говорити'], ['call', 'кликати, дзвонити'], ['ask', 'питати, просити'], ['talk', 'розмовляти'], ['meet (met, met)', 'знайомитися (зустрічати)'], ['understand (understood, understood)', 'розуміти'], ['speak (spoke, spoken)', 'говорити'], ['allow', 'дозволяти'], ['offer', 'пропонувати'], ['consider', 'розглядати, вважати'], ['suggest', 'пропонувати'], ['require', 'вимагати, потребуватиме'], ['report', 'доповідати'], ['explain', 'пояснювати'], ['thank', 'дякувати'], ['agree', 'погоджуватися'], ['describe', 'описувати'], ['represent', 'представляти (напр', ' компанію)'], ['lie', 'брехати'], ['tell the truth (told, told)', 'говорити правду'], ['mean (meant, meant)', 'мати на увазі'], ['argue', 'сперечатися'], ['wonder', 'цікавитися'], ['name', 'називати, іменувати'], ['answer', 'відповідати'], ['state', 'робити заяву'], ['discuss', 'обговорювати'], ['laugh', 'сміятися'], ['guess', 'здогадуватися'], ['prove', 'доводити'], ['sound', 'звучати'], ['respond', 'відповідати'], ['reveal', 'виявляти, розкривати'], ['treat', 'лікувати (звертатися з будь-ким)'], ['affect', 'впливати (впливати)'], ['mention', 'згадувати'], ['care', 'піклуватися, турбуватися, ставитися не байдуже'], ['avoid', 'уникати'], ['support', 'підтримувати'], ['sing (sang, sung)', 'співати'], ['address', 'звертатися до когось'], ['smile', 'посміхатися'], ['admit', 'визнати'], ['assume', 'припускати'], ['refer', 'посилатися на щось, направляти, посилати'], ['announce', 'оголошувати'], ['encourage', 'надихати, заохочувати, спонукати'], ['introduce', 'представляти (напр', ' однієї людини іншій)'], ['refuse', 'відмовлятися'], ['express', 'висловлювати'], ['settle', 'залагоджувати (питання)'], ['cry', 'плакати (кричати)'], ['insist', 'наполягати'], ['ignore', 'нехтувати'], ['deny', 'заперечувати'], ['promise', 'обіцяти'], ['demand', 'вимагати'], ['welcome', 'вітати'], ['invite', 'запрошувати'], ['repeat', 'повторювати'], ['recommend', 'рекомендувати'], ['propose', 'пропонувати'], ['declare', 'оголошувати'], ["matter (It doesn't matter)", 'мати значення'], ['judge', 'судити, засуджувати'], ['ensure', 'забезпечувати (гарантувати, переконуватися в чомусь)'], ['challenge', 'кидати виклик'], ['warn', 'попереджати'], ['influence', 'впливати'], ['blame', 'звинувачувати'], ['complain', 'скаржитися'], ['back', 'підтримувати, відступати'], ['cite', 'цитувати (посилатися)'], ['emphasize', 'підкреслювати (робити наголос на чомусь)'], ['decline', 'відхиляти (напр', ' пропозиція)'], ['accuse', 'звинувачувати'], ['reject', 'відкидати'], ['convince', 'переконувати'], ['approve', 'підтверджувати, схвалювати'], ['list', 'перераховувати, складати список'], ['permit', 'дозволяти'], ['scream', 'кричати'], ['shout', 'викрикувати, кричати'], ['inform', 'інформувати'], ['bother', 'турбувати'], ['reply', 'відповідати'], ['resolve', 'вирішувати питання)'], ['contact', "контактувати, зв'язуватися"], ['interview', "проводити інтерв'ю (бесіду)"], ['quote', 'цитувати'], ['urge', 'квапити, переконувати'], ['whisper', 'шепотіти'], ['favor (favour)', 'надавати увагу, бути прихильним'], ['comment', 'коментувати'], ['negotiate', 'вести переговори'], ['advise', 'радити'], ['criticize', 'критикувати'], ['assure', 'запевняти'], ['yell', 'кричати'], ['communicate', 'спілкуватися'], ['disagree', 'не погоджуватися'], ['proceed', 'переходити до чогось, продовжувати як заплановано'], ['translate', 'переводити (лингв', ')'], ['interpret', 'тлумачити, інтерпретувати, перекладати (усно)'], ['pause', 'робити паузу'], ['imply', 'припускати, мати на увазі, натякати'], ['respect', 'поважати'], ['characterize', 'характеризувати'], ['appeal', 'звертатися, апелювати'], ['stress', 'робити наголос'], ['doubt', 'сумніватися'], ['guarantee', 'гарантувати'], ['honor', 'шанувати, поважати'], ['encounter', 'зустрічати (випадково зустріти когось)'], ['dominate', 'домінувати, мати повний контроль'], ['accept', 'приймати'], ['let (let, let)', 'дозволяти'], ['date', 'зустрічатися, ходити на побачення']]
    elif k == 7:
        l=[['win (won, won)', 'перемагати'], ['kill', 'вбивати'], ['hit (hit, hit)', 'вдарити'], ['fight (fought, fought)', 'битися'], ['shoot (shot, shot)', 'стріляти (знімати на камеру)'], ['protect', 'захищати'], ['force', 'примушувати'], ['beat (beat, beaten)', 'бити'], ['hurt (hurt, hurt)', 'завдавати болю'], ['strike (struck, struck)', 'ударяти (страйкувати)'], ['threaten', 'загрожувати'], ['destroy', 'знищувати'], ['fire', 'стріляти'], ['attack', 'атакувати'], ['struggle', 'боротися'], ['capture', 'захоплювати'], ['defend', 'захищати'], ['kick', 'штовхати'], ['eliminate', 'усувати'], ['score', 'набирати очки (бали)'], ['aim', 'цілитися'], ['compete (sport)', 'змагатися'], ['confront', 'протистояти'], ['resist', 'чинити опір'], ['target', 'робити мішенню, цілитися'], ['overcome', 'долати'], ['give up (gave, given)', 'здаватися'], ['surrender', 'здаватися']]
    elif k == 8:
        l=[['cost (cost, cost)', 'коштувати'], ['earn', 'заробляти'], ['make money (made, made)', 'заробляти'], ['promote', 'просувати, рекламувати, підвищувати по службі'], ['charge', 'брати плату'], ['estimate', 'оцінювати'], ['account', 'вважати, вести облік'], ['invest', 'інвестувати'], ['assess', 'оцінювати'], ['compete', 'конкурувати'], ['purchase', 'купувати'], ['evaluate', 'оцінювати'], ['trade', 'торгувати'], ['market', 'просувати на ринку (рекламувати)'], ['withdraw', 'знімати (гроші з рахунку в банку)'], ['convert', 'конвертувати'], ['spend (spent, spent)', 'витрачати (напр', ' гроші), проводити час'], ['buy (bought, bought)', 'купувати'], ['sell (sold, sold)', 'продавати'], ['deal (dealt, dealt)', 'вести справи'], ['produce', 'виробляти'], ['save', 'робити заощадження, економити'], ['rule', 'правити (панувати)'], ['elect', 'вибирати (на виборах)'], ['vote', 'голосувати'], ['contribute', 'робити внесок у щось'], ['settle', 'розселятися (створювати поселення)'], ['impose', 'накладати (напр', " зобов'язання)"], ['transfer', 'передавати, переводити (напр', ' гроші)'], ['distribute', 'поширювати'], ['deposit', 'вносити гроші (на рахунок в банку)'], ['afford', 'повзволять собі']]
    elif k == 9:
        l=[['live', 'жити'], ['grow up (grew, grown)', 'рости'], ['die', 'померти'], ['be born', 'бути народженим'], ['marry (get married)', 'одружитися (виходити заміж)'], ['survive', 'виживати'], ['adopt', 'всиновлювати (удочеряти)'], ['retire', 'виходити на пенсію'], ['breathe', 'дихати'], ['kiss', 'цілувати'], ['bury', 'ховати'], ['pray', 'молитися'], ['graduate', 'випускатися з навчального закладу'], ['tire (get tired)', 'втомлюватися'], ['adapt', 'адаптувати (-ся)'], ['pretend', 'прикидатися'], ['divorce (get divorced)', 'розлучатися (про подружжя)'], ['inherit', 'успадковувати']]
    elif k == 10:
        l=[['sleep (slept, slept)', 'спати'], ['dress', 'одягати (-ся)'], ['wake up (woke, woken)', 'будити (прокидатися)'], ['eat (ate, eaten)', 'є'], ['drink (drank, drunk)', 'пити, випивати'], ['feed (fed, fed)', 'годувати'], ['cook', 'готувати їжу'], ['taste', 'пробувати на смак, відчуватися на смак'], ['bake', 'піч'], ['freeze', 'заморожувати, замерзати, зберігати в морозилці'], ['play', 'грати в гру або на музичному інструменті, відтворювати запис'], ['spend (spent, spent)', 'проводити (напр', ' час), витрачати гроші'], ['enjoy', 'насолоджуватися'], ['visit', 'відвідувати'], ['travel', 'подорожувати, їхати (переміщатися)'], ['rest', 'відпочивати'], ['dance', 'танцювати'], ['celebrate', 'святкувати'], ['bet (bet, bet)', 'робити ставку'], ['relax', 'розслаблятися'], ['gamble', 'грати в азартні ігри'], ['have fun (had, had)', 'розважатися (веселитися)']]
    elif k == 11:
        l=[['weigh', 'важити, зважувати'], ['balance', 'балансувати'], ['flow (flew, flown)', 'протікати'], ['transform', 'трансформувати (-ся), значно змінювати (ся)'], ['recover', 'відновлювати (-ся), видужувати'], ['expose', 'виставляти (піддавати чогось)'], ['pop', 'плескати (вискакувати)'], ['indicate', 'вказувати (пояснювати)'], ['alter', 'змінювати, модифікувати'], ['alternate', 'чергувати'], ['double', 'подвоювати'], ['retain ', 'утримувати'], ['fade', "в'янути (бліднуть)"], ['form', 'формувати'], ['shape', 'надавати форму'], ['change', 'змінювати'], ['place', 'розміщувати'], ['rise (rose, risen)', 'піднімати (-ся)'], ['reflect', 'відображати (-ся)'], ['enable', 'включати (активувати), робити можливим'], ['wave', 'майоріти, махати'], ['snap', 'клацати, тріщати, зламати з хрускотом'], ['display', 'показувати (виставляти на показ)'], ['stick', 'липнути']]
    elif k == 12:
        l=[['testify', 'давати свідчення'], ['justify', 'виправдовувати'], ['violate', 'порушувати'], ['witness', 'бути свідком'], ['arrest', 'заарештовувати'], ['investigate', 'розслідувати'], ['confess ', 'зізнаватися'], ['accuse', 'звинувачувати'], ['charge', 'звинувачувати (офіційно)'], ['suspect', 'підозрювати'], ['sue', 'подавати в суд'], ['convict', 'виносити вирок, визнавати винним'], ['beat (up) (beat, beaten)', 'бити, бити'], ['murder', 'вбивати'], ['kill', 'вбивати'], ['attack', 'нападати'], ['free', 'освободжать'], ['offend', 'ображати'], ['disturb', 'турбувати'], ['steal (stole, stolen)', 'красти'], ['rob', 'грабувати'], ['rape', 'гвалтувати'], ['punish', 'карати'], ['do time', 'сидіти в тюрмі)'], ['interrogate ', 'допитувати'], ['swear', 'клястися']]
    elif k == 13:
        l=[['reach', 'досягати (дотягуватися)'], ['catch (caught, caught)', 'ловити'], ['drop', 'упускати'], ['hang (hung, hung)', 'повісити'], ['touch', 'торкатися'], ['clear', 'очищати'], ['pour', 'лити (напр', ' воду)'], ['stir', 'перемішувати'], ['clean', 'чистити, прибирати (мити, приводити в порядок)'], ['wrap', 'загортати'], ['wash', 'прати (мити)'], ['ring (rang, rung)', 'дзвонити'], ['embrace', 'обіймати'], ['hug', 'обіймати'], ['put (put, put)', 'класти (поміщати)'], ['use', 'використовувати'], ['show', 'показувати'], ['hold (held, held)', 'тримати'], ['open', 'відкривати'], ['cut', 'різати'], ['pull', 'тягнути'], ['break (broke, broken)', 'ламати'], ['cover', 'прикривати'], ['draw (drew, drawn)', 'тягнути'], ['point', 'вказувати (на що-небудь)'], ['close', 'закривати'], ['replace', 'замінювати'], ['collect', 'збирати, забирати'], ['grab', 'вистачати'], ['tie', "пов'язувати"], ['press', 'тиснути'], ['link', "з'єднувати, проводити зв'язок між фактами"], ['mix', 'перемішувати'], ['stretch', 'розтягувати'], ['hand', 'подавати щось, передавати з рук в руки'], ['knock', 'стукати'], ['bend (bent, bent)', 'гнути'], ['lock', 'замикати на замок'], ['tear (tore, torn)', 'рвати'], ['pack', 'упаковувати'], ['attach', 'прикріплювати'], ['dig (dug, dug)', 'копати'], ['bind (bound, bound)', "пов'язувати (мотузкою)"], ['wind (wound, wound)', 'закручувати'], ['wipe', 'протирати'], ['load', 'завантажувати'], ['sweep (swept, swept)', 'помсти'], ['squeeze', 'стискати'], ['rub', 'терти'], ['tap', 'постукувати'], ['spin (spun, spun)', 'обертати'], ['plant', 'садити (рослина)'], ['pick', 'вибирати'], ['gather', 'збирати (разом)'], ['hide (hid, hid)', 'ховати (ся)'], ['blow (blew, blown)', 'дути'], ['smoke', 'курити'], ['act', 'діяти'], ['do (did, done)', 'робити'], ['demonstrate', 'демонструвати'], ['lean', 'притулятися, нахилятися'], ['fix', 'лагодити'], ['nod', 'кивати'], ['pose', 'позувати'], ['send (sent, sent)', 'відправляти'], ['burn (burnt, burnt)', 'спалювати'], ['shut (shut, shut)', 'закривати'], ['line (up)', 'вибудовувати в лінію'], ['arrange (the books on the shelves)', 'приводити в порядок (розставляти)'], ['install', 'встановлювати']]
    full=len(l)
    add=0
    u=0
    u=1
    number_temp = 1
    number_all = len(l)
    prav = 0
    if q==1:
        while len(l)!=0:
            print(number_temp, '/', number_all)
            u+=1
            i=random.randint(0, len(l)-1)
            cprint(l[i][0], 'green')
            o=input(': ')
            print(l[i][1])
            r=str(input())
            if r=='':
                l.remove(l[i])
                prav+=1
            elif r=='0':
                break
            else:
                add+=1
                number_all+=1
            print('---------------')
            number_temp+=1
    else:
        while len(l)!=0:
            print(number_temp, '/', number_all)
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
                number_all+=1
            print('---------------')
            number_temp+=1
    res = (100*prav)/(full+add)
    print(int(res), "%")
