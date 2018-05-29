import xlrd
import json
import requests
base_url="http://127.0.0.1:5006"
wb=xlrd.open_workbook('ceshiyongli.xlsx')
sh=wb.sheet_by_index(0)
# print(sh.cell(1,1).value)
bpl='''def {case_name}():
    url=base_url+"/add/?a={a}&b={b}"
    res=requests.get(url)
'''
for row in range(1,sh.nrows):
    name=sh.cell(row,0).value
    url=sh.cell(row,1).value
    methode=sh.cell(row,2).value
    data_type=sh.cell(row,3).value
    a=sh.cell(row,4).value
    b=sh.cell(row,5).value
    excepted=sh.cell(row,6).value
    actual=sh.cell(row,7).value
    status=sh.cell(row,8).value
    case=bpl.format(case_name=name,a=a,b=b)
    exec(case)
    
