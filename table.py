class Table:
    def __init__(self,dataframe):
        self.name=dataframe.iloc[0][1]
        self.source=(dataframe.iloc[2][1])[16:]
        print(dataframe)
        self.prompts=[]
        i=3
        while True:
            if dataframe.iloc[i][0]==None and dataframe.iloc[i][1]== None:
                break
            elif type(dataframe.iloc[i][0])==str and "【出力列" in dataframe.iloc[i][0]:
                break
            elif dataframe.iloc[i][1]!=None:
                self.prompts.append(dataframe.iloc[i][1])
                i=i+1
