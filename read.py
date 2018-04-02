import pandas as pd
import report
import table
xls=pd.ExcelFile('file.xlsx')

#read
all_sheets= pd.read_excel(xls,None)
for sheet in list(all_sheets.keys()):
    content=pd.read_excel(xls,sheet)
    new_report= report.report(list(content)[1])
    first=4
    last=first
    for last in range(4,content.shape[0]+1):
        if last==content.shape[0]or(type(content.iloc[last][0])==str and "【表名】" in content.iloc[last][0] and last!=first) or (content.iloc[last][0] == None and content.iloc[last][1]==None) :
            new_report.addTable(table.Table(content.truncate(first,last-1,0,True)))
            first=last            
    new_report.export()
    
    
