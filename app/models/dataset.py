import pandas as pd

#Class
class ModelsDataset():
     
    def leitura_csv(self,dataset_local):
        df = pd.read_csv(dataset_local)
        return df    

    