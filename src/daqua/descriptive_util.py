

from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
import numpy as np
import pandas as pd
import os
import datetime

class MetaInfo:


    def __init__(self, main):        
        self.main = main
        self._dfs = {sheet_name: self.main.excel_reader.parseExcel(sheet_name) for 
                        sheet_name in self.main.excel_reader.getSheetNames()}
        self._meta_data = pd.DataFrame([{
                                sheet_name: dataframe.shape for sheet_name, dataframe in self._dfs.items()
                            }])

        self._detailed_meta = {sheet_name: self.calculateDetailMeta(sheet_name) for sheet_name in self._dfs.keys()}
        self._descriptive_num = {sheet_name: self.getNumericDetails(sheet_name) for sheet_name in self._dfs.keys()}
        self._descriptive_str = {sheet_name: self.getStringDetails(sheet_name) for sheet_name in self._dfs.keys()}
        self._descriptive_numeric = {sheet_name: self.getDfWiseDetails(sheet_name)[1] for sheet_name in self._dfs.keys()}
        self._quantile_numeric = {sheet_name: self.getDfWiseDetails(sheet_name)[0] for sheet_name in self._dfs.keys()}

        # self._descriptive_date = {sheet_name: self.detectDate(sheet_name) for sheet_name in self._dfs.keys()}


    def getDfs(self):
        return self._dfs
    

    def getMetaData(self):
        return self._meta_data.T

    
    def getDetailMeta(self):
        return self._detailed_meta


    def descriptiveNumeric(self):
        return self._descriptive_numeric


    def quantileStat(self):
        return self._quantile_numeric

        
    def calculateDetailMeta(self, sheet_name):
        df = self._dfs[sheet_name]
        column_names = df.columns.tolist()
        detailed_meta = [
                        {
                            "column_name": col,
                            "data_type": df[col].dtype,
                            "not_na_val": df[col].notna().sum(),
                            "fill_rate": df[col].notna().sum()*100/len(df),
                            "num_unique": df[col].nunique()
                        }
                        for col in column_names]

        detailed_meta_df = pd.DataFrame(detailed_meta)
        detailed_meta_df.loc[:, 'unique_rate'] = detailed_meta_df.loc[:, 'num_unique'] * 100 / detailed_meta_df.loc[:, 'not_na_val']
        detailed_meta_df.loc[:, 'unique_rate'] = detailed_meta_df.loc[:, 'unique_rate'].fillna(0)
        return detailed_meta_df


    def getAllMeta(self):
        return self._all_meta_df

    
    def getNumericDetails(self, sheet_name):
        df = self._dfs[sheet_name]
        meta_df = self._detailed_meta[sheet_name]
        num_cols = meta_df.loc[(meta_df['data_type']==int)|(meta_df['data_type']==float), 'column_name'].tolist()
        return num_cols


    def getStringDetails(self, sheet_name):
        df = self._dfs[sheet_name]
        meta_df = self._detailed_meta[sheet_name]
        str_cols = meta_df.loc[meta_df['data_type']==str, 'column_name'].tolist()
        return str_cols


    def detectDate(self, sheet_name):
        df = self._dfs[sheet_name]
        mask = df.astype(str).apply(lambda x : x.str.match(r'\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2}').all())
        df.loc[:,mask] = df.loc[:,mask].apply(pd.to_datetime)
        date_time_cols = df[df.dtypes == datetime.datetime]
        return date_time_cols

    
    def getStatData(self, col_series, data):
        quantile_stat = {
                            "column_name": col_series,
                            "max_val": data[col_series].max(),
                            "min_val": data[col_series].min(),
                            "Range": data[col_series].max() - data[col_series].min(),
                            "5_th_percentile": data[col_series].quantile(0.05),
                            "95_th_percentile": data[col_series].quantile(0.95),
                            "Q1": np.percentile(data[col_series], 25),
                            "Q3": np.percentile(data[col_series], 75),
                            "IQR": np.percentile(data[col_series], 25) - np.percentile(data[col_series], 75),
                            "Median": np.percentile(data[col_series], 50),
                        }
        descriptive_stat = {
            "column_name": col_series,
            "standard_deviation": data[col_series].std(),
            "Mean": data[col_series].mean(),
            "Median Absolute Deviation": data[col_series].mad(),
            "Skewness": data[col_series].skew(),
            "Sum": data[col_series].sum(),
            "Variance": data[col_series].var(),
            "Monotonicity": data[col_series].is_monotonic
        }
        return quantile_stat, descriptive_stat


    def getDfWiseDetails(self, sheet_name):
        df = self._dfs[sheet_name][self._descriptive_num[sheet_name]]
        quant_lst, desc_lst = [], []
        for item in df:
            res1, res2 = self.getStatData(item, df)
            quant_lst.append(res1)
            desc_lst.append(res2)
        quant_df = pd.DataFrame.from_dict(quant_lst)
        desc_df = pd.DataFrame.from_dict(desc_lst)
        return quant_df, desc_df