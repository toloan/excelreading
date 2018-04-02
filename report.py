#dictionary

class report:

    def __init__(self,name):
        self.dictionary={ 'media':'string','account_no':'string','from_date':'date','to_date':'date','device':'string','network':'string','month':'string','rowtype':'string','list_type':'string','row_type':'string','type':'string','deliver':'string'}
        self.name=name
        self.tables =[]
    def addTable(self,new_table):
        add=True
        for table in self.tables:
            if len(set(table.prompts).intersection(new_table.prompts))==len(set(table.prompts)) and len(set(table.prompts).intersection(new_table.prompts))==len(set(new_table.prompts)) and table.source==new_table.source:
                print("soánh")
                print(table.source==new_table.source)
                add=False
        if add==True:
            self.tables.append(new_table)
    def export(self):
        for table in self.tables:
            file=open(self.name+"_"+table.name+".txt","w",encoding="utf-8")
            content="Select * \n From standard_report."+table.source+" as "+table.source+"\n where \t"
            for prompt in table.prompts:
                content=content+table.source+"."+prompt+"=#prompt('"+prompt+"','"+self.dictionary[prompt]+"')# and\n"
            file.write(content)
            file.close()
        
