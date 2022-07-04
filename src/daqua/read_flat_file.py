"""
Created By: Satya Pati
Created on: 17-06-2021 00:36
"""


import pandas as pd
import numpy as np
import os
import datetime
import time
from datetime import datetime, timedelta


class ReadFlatFile:
    """
    This is the super class to read all the flat files
    """
    def __init__(self, main):
        self.main = main
        self.file_path = self.main.config.file_path
        self.file_types = ['csv', 'excel', 'json']
        _,self.fileExtension = os.path.splitext(self.file_path)
        self.file_size = str(os.path.getsize(self.file_path)/(1024*1024)) + ' MB'
        self._res_dict = {
                                "file_name": self.file_path.split(os.path.sep)[-1],
                                "file_type": self.fileExtension,
                                "file_size": self.file_size
                            }


    def getFileDetails(self):
        """
        This function will return meta info
        """
        return self._res_dict


class ReadExcel(ReadFlatFile):
    """
    This is the class to read excel files
    """   
    def __init__(self, main):
        super().__init__(main)
        self._excel_file = pd.ExcelFile(self.file_path)
        self._sheet_names = self._excel_file.sheet_names
        self._res_dict['n_tables'] = len(self._sheet_names)


    def readExcelFile(self):
        return self._excel_file


    def getSheetNames(self):
        return self._sheet_names


    def parseExcel(self, sheet_name):
        df = self._excel_file.parse(sheet_name)
        return df
