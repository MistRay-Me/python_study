# coding=utf-8
# 写
import xlwt
# 读
import xlrd
import os
import xlutils

if __name__ == '__main__':
    write_book = xlwt.Workbook()  # 打开一个excel
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    sheet = write_book.add_sheet('test')  # 在打开的excel中添加一个sheet
    sheet.write(1, 2, '122233')  # 写入excel，i行0列
    sheet.write(2, 3, '11111')
    write_book.save('/Users/zhangjunyi/Desktop/answer.xls')
