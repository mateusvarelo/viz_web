from dataset import Dataset

#class
#Pata modelar os dados que contém minhas informações, irei utilizar lib pandas
# e para deixar o dado no formato em que a lib entenda, preciso utilizar datafram , formato tabular.
class ModelsDataFrame():
    def __init__(self) -> None:
        dtset = Dataset()
    def gera_dataframe(self):
       obj_df =  self.dtset.leitura('dataset/spotify')
       return obj_df
   
