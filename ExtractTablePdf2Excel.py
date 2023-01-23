import tabula
 
table = tabula.read_pdf('/Users/magnetosa/Python/rcs/TableandText.pdf', pages=1)
table[0].to_excel('output.xlsx', index=None)