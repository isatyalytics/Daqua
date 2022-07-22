"""
This module aims to read the flat files like excel, csv, json, SAS, parquet files
and return the dataframe and meta files
"""

import os
import pandas as pd


class ReadFlatFile:
    """
    A super class to operate on flat files.

    Attributes
    ----------
    file_path : str
        path to the flat file
    file_type : str
        Type of file
    file_extension : str
        extension of the given file
    file_size: str
        Size of the uploaded file
    _res_dict: dict
        The resultant dictionary which contains other attributes like,
        file_name, file_type and file_size

    Methods
    -------
    get_file_details() -> dict
        return _res_dict.
    """

    def __init__(self, file_path: str, file_type: str = None) -> None:
        """
        Constructor function for ReadFlatFile class.

        Param
        -----
        file_path: str
            Path to the file
        file_type: str
            Type of the file. by default, it's None. Should accept CSV, Excel, Json and Parquet
        """
        # TODO: Add Exception when file type is not in [CSV, Excel, Json, Pickle and Parquet]
        # TODO: Raise Exception when the file path is not found => File Not Found Error

        self.file_path = file_path
        if file_type:
            self.file_type = file_type.lower()
        _, self.file_extension = os.path.splitext(self.file_path)
        self.file_size = str(os.path.getsize(self.file_path) / (1024 * 1024)) + ' MB'
        self._n_tables: int = 0
        self._res_dict: dict = {
            "file_name": self.file_path.split(os.path.sep)[-1],
            "file_type": self.file_extension,
            "file_size": self.file_size
        }

    def get_file_details(self) -> dict:
        """
        This function will return meta info
        """
        return self._res_dict


class ReadExcel(ReadFlatFile):
    """
    This is the class to read Excel files

    Attributes
    -----------
        _excel_file: pd.ExcelFile object
            Excel File objects
        _sheet_names: list
            Name of the sheets present
        _n_tables: int
            Number of sheets present in that Excel
    Methods
    -------
        read_excel_file() -> pd.ExcelFile
            Return pd.ExcelFile object which is created inside __init__.
        get_sheet_names() -> list
            Return the list of sheet names

    """

    def __init__(self, file_path: str, file_type: str = None) -> None:
        super().__init__(file_path)
        if file_type:
            self.file_type = file_type.lower()
        self._excel_file = pd.ExcelFile(self.file_path)
        self._sheet_names = self._excel_file.sheet_names
        self._n_tables = len(self._sheet_names)
        self._res_dict['num_tables'] = self._n_tables

    def read_excel_file(self) -> pd.ExcelFile:
        """ Return the ExcelFile object """
        return self._excel_file

    def get_sheet_names(self) -> list[str]:
        """ Return the list of sheets present in that Excel file  """
        return self._sheet_names

    def read_sheet(self, sheet_name: str) -> pd.DataFrame:
        """ Read a particular Excel sheet as a dataframe """
        res_df = self._excel_file.parse(sheet_name)
        return res_df


class ReadCSV(ReadFlatFile):
    """ Reading CSV file and return the meta about file and the dataframe

    Attributes:
        _df: pd.DataFrame
            After reading the csv file, the resultant dataframe
    Methods:
        get_df() -> pd.DataFrame
            return the resultant dataframe
        get_df_size() -> tuple
            return the shape of the dataframe
    """

    def __init__(self, file_path: str, **kwargs: dict) -> None:
        super().__init__(file_path)
        self._df = pd.read_csv(self.file_path, engine='c', **kwargs)

    def get_df(self) -> pd.DataFrame:
        """ Return the DataFrame """
        return self._df

    def get_df_size(self) -> tuple:
        """ Return the size of the dataframe """
        return self._df.shape


class ReadJson(ReadFlatFile):
    """ Reading Json file and return the meta about file and the dataframe

        Attributes:
            _df: pd.DataFrame
                After reading the csv file, the resultant dataframe
        Methods:
            get_df() -> pd.DataFrame
                return the resultant dataframe
            get_df_shape() -> tuple
                return the shape of the dataframe
    """

    def __init__(self, file_path: str, **kwargs: dict) -> None:
        """ Creating Pandas dataframe from Json """
        super().__init__(file_path)
        self._df = pd.read_json(file_path, **kwargs)

    @property
    def get_df(self) -> pd.DataFrame:
        """ Return the resultant DataFrame """
        return self._df

    def get_df_shape(self) -> tuple[int]:
        """ Return the shape of the dataframe """
        return self._df.shape
