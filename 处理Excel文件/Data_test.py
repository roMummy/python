import xlrd
import io , sys  #设置系统输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')  
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8') 
# reload(sys)
# sys.setdefaultencoding("utf8")

book = xlrd.open_workbook("SOWC 2014 Stat Tables_Table 9.xlsx")

# for sheet in book.sheets():#找到表名
# 	print(sheet.name)

sheet = book.sheet_by_name("Table 9 ")
# print(sheet) 
# print(dir(sheet))
count = 0
for i in range(sheet.nrows):
	if count < 20:
		if i >= 14:
			row = sheet.row_values(i)
			print(i,row)
		count += 1
		

