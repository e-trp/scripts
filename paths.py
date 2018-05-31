#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import hashlib
import pandas as pd
import time

# разбирает все файлы в директории по папкам с названием
# расширений файлов
def fdistribution(path='.', exclude=('downloads.py',)):
    exds = []
    os.chdir(path)
    curpath=os.getcwd()
    f_in_dir=os.listdir(curpath)
    for f in f_in_dir:
        if os.path.isfile(f) and f not in exclude:
            exds.append(f)
    print(exds)
    for f in exds:
        filename, file_extension = os.path.splitext(f)
        try:
            if not os.path.isdir(file_extension[1:]):
                np=os.path.abspath(os.path.join(curpath,file_extension[1:]))
                os.makedirs(np)
            fr=os.path.abspath(os.path.join(curpath,f))
            to=os.path.abspath(os.path.join(curpath, file_extension[1:], f))
            os.rename(fr,to)
        except Exception as err:
            print(err)

# создает таблицу из файлов в директории и всех поддиректориях
# в каждой записи название, путь, размер в мб, хэш, дата последнего изменения
# может выдавать данные по отдельному файлу и импортировать всю таблицу в csv
class HashTable():

    def __init__(self, dir='.'):
        self.dir=dir
        self.get_files()


    def get_files(self):
        files=[]
        try:
            for rootdir, dirnames, filenames in os.walk(self.dir):
                for name in filenames:
                    fp=os.path.abspath(os.path.join(rootdir,name))
                    dt=os.stat(fp)
                    z=dt.st_size/ 2 ** 20
                    h=self.make_hash(fp)
                    files.append([ name, fp, h, z, time.ctime(dt.st_mtime)])

        except:
            pass
        self.pf = pd.DataFrame(files, columns=['fname', 'path', 'fhash', 'fsize_mb', 'mod_t'])
        del files

    def to_csv(self):
        self.pf.to_csv('files.csv', sep=',', encoding='utf-8')

    def make_hash(self, file, block=1024):
        h = hashlib.new('sha1')
        with open(file, 'rb') as file_desc:
            buf = file_desc.read(block)
            while len(buf) > 0:
                h.update(buf)
                buf = file_desc.read(block)
        return h.hexdigest()

    def get_finfo(self, fname):
        return self.pf[self.pf['fname'].str.contains(fname)]