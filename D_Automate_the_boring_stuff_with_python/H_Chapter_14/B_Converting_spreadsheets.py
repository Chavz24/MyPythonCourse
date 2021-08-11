"""Este programa descarga un google spreadsheet en los formatos.xlsx,.pdf,.CSV"""

import ezsheets

ss=ezsheets.Spreadsheet('MiContabilidad')

ss.downloadAsCSV()
ss.downloadAsExcel()
ss.downloadAsPDF()