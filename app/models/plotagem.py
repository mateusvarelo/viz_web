from dataset import ModelsDataFrame




def plota_grafico(self):
        obj_df = ModelsDataFrame()
        df = obj_df.gera_dataframe()
        return df
plot = Plotly()
print(plot.plota_grafico().head())        