from daqua.data_source_connection.read_flat_file import ReadFlatFile, ReadCSV, ReadExcel, ReadJson
from daqua.model.model import Daqua


class Main:
    def __init__(self):
        pass

    def read_csv(self, csv_path):
        csv_reader = ReadCSV(csv_path)
        df_shape = csv_reader.get_df_size()
        _df = csv_reader.get_df()
        dq_obj = Daqua(_df)
        return dq_obj

    def read_excel(self, excel_path):
        excel_reader = ReadExcel(excel_path)
        excel_file_obj = excel_reader.read_excel_file()
        sheet_names = excel_reader.get_sheet_names()
        for sheet in sheet_names:
            _df = excel_reader.read_sheet(sheet)
            yield {sheet: Daqua(_df)}

