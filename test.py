import os,pandas as pd, numpy as np

sheet_names = ['花境苗木分类清单','春季','夏季','秋季','冬季']
file_name = '四季花境苗木.xls'
fleurnames = []
for sheetname in sheet_names:
    fleurlist1 = pd.read_excel(file_name,sheet_name=sheetname).iloc[2:,1].values.ravel().tolist()
    fleurnames.extend([{x:sheetname} for x in fleurlist1])
# fleurnames = [x for x in list(set(fleurnames)) if type(x) == str]
# fleurnames.sort()

def get_pictures(keywowrd):
    cmd = 'googleimagesdownload -k %s -l 5 -o download/%s'%(list(keywowrd.keys())[0],list(keywowrd.values())[0])
    os.system(cmd)

if __name__=="__main__":
    from multiprocessing.dummy import  Pool
    p = Pool(50)
    p.map(get_pictures, fleurnames)
