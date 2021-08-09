#Creando graficos de excel
import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']


for i in range(1,11):
    sheet['A'+str(i)]=i

rej_obj=openpyxl.chart.Reference(sheet,min_row=1,min_col=1,max_row=10,max_col=1)
series_obj=openpyxl.chart.Series(rej_obj,title='Uno')
chart_obj=openpyxl.chart.PieChart()
chart_obj.title='My chart'
chart_obj.append(series_obj)

sheet.add_chart(chart_obj,'C6')



wb.save('mychartobj.xlsx')


