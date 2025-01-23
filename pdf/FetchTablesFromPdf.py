from typing import List, Optional

import pandas as pd
import tabula


class PDFTableExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.tables: List[pd.DataFrame] = []

    def exttract_tables(self,
                        pages: str = all,
                        lattice: bool = True,
                        stream: bool = False
                        ) -> List[pd.DataFrame]:
        """
        从PDF中提取表格
        参数：
        :param pages: 页码范围 例如 ‘1-3’或 all
        :param lattice: 是否使用lattice模式 （适用于有网格线的表格）
        :param stream:  是否使用stream模式 （适用于没有网格线的表格）
        :return:
        """
        try:
            self.tables = tabula.read_pdf(
                self.pdf_path,
                pages=pages,
                multiple_tables=True,
                lattice=lattice,
                stream=stream
            )
            print(f"成功从PDF中提取表格：{len(self.tables)} 个")
            return self.tables
        except Exception as e:
            print(f"提取表格时出错：{str(e)}")
            return []

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        清理数据 表格数据
        :param df:
        :return:
        """
        # 删除全为空的行
        df = df.dropna(how='all')
        # 删除全为空的列
        df = df.dropna(axis=1, how='all')
        # 填充空值
        df = df.fillna("")
        return df

    def export_to_excel(self,
                        output_path: str,
                        sheet_names: Optional[List[str]] = None) -> None:
        """
        将表格导出到EXCEL
        :param output_path: EXCEL文件保存路径
        :param sheet_names: EXCEL sheet名
        :return:
        """
        try:
            if not self.tables:
                print("没有数据表导出")
                return
                # 创建EXCEL写入器
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                for i, table in enumerate(self.tables):
                    clean_table = self.clean_data(table)

                    # 设置工作表名称
                    sheet_name = f"Table_{i + 1}"
                    if sheet_names and i < len(sheet_names):
                        sheet_name = sheet_names[i]
                    # 写入EXCEL
                    clean_table.to_excel(writer,
                                         sheet_name=sheet_name,
                                         index=False)
                    print(f"数据导出成功：{output_path}")
        except Exception as e:
            print(f"导出EXCEL异常：{str(e)}")


if __name__ == '__main__':
    pdf_file = "D:\\tmp\\转让公告\\24北银-8.pdf"
    excel_file = "D:\\tmp\\转让公告\\a.xlsx"
    extractor = PDFTableExtractor(pdf_file)
    tables = extractor.exttract_tables(pages='all')
    sheet_names = ['sheet1', 'sheet2', 'sheet3']
    extractor.export_to_excel(excel_file, sheet_names)
