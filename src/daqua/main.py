"""
Created By: Satya Pati
Created on: 17-06-2021 00:36
"""
import numpy as np
import pandas as pd


from daqua.config import Config
import daqua.read_flat_file as read_flat_file
import daqua.descriptive_util as descriptive_util

class Daqua:
    def __init__(self):
        self.config = None
        self.excel_reader = None
        self.meta_info = None


    def read_excel(self, path):
        self.config = Config(path)
        self.excel_reader = read_flat_file.ReadExcel(self)
        self.meta_info = descriptive_util.MetaInfo(self)


    def getDataFrames(self):
        res = self.meta_info.getDfs()
        return res


    def getMetaData(self):
        res = self.meta_info.getMetaData()
        return res


    def getDetailedMeta(self):
        res = self.meta_info.getDetailMeta()
        return res

    
    def getNumericDesc(self):
        res = self.meta_info.descriptiveNumeric()
        return res


    def getQuantileStat(self):
        res = self.meta_info.quantileStat()
        return res
