import xlsxwriter 
    
# Workbook() takes one, non-optional, argument   
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('chart_Line.xlsx') 
    
# The workbook object is then used to add new   
# worksheet via the add_worksheet() method.  
worksheet = workbook.add_worksheet() 
    
# Create a new Format object to formats cells 
# in worksheets using add_format() method . 
    
# here we create bold format object . 
bold = workbook.add_format({'bold': 1}) 
    
# create a data list . 
headings = ['Number', 'Batch 1', 'Batch 2'] 
    
data = [ 
    [0, 2, 3, 7, 10], 
    [80, 80, 100, 60, 50], 
    [10, 4, 8, 4, 5], 
] 

# Write a row of data starting from 'A1' 
# with bold format . 
worksheet.write_row('A1', headings, bold) 
    
# Write a column of data starting from  
# 'A2', 'B2', 'C2' respectively . 
worksheet.write_column('A2', data[0]) 
worksheet.write_column('B2', data[1]) 
worksheet.write_column('C2', data[2]) 
    
# Create a chart object that can be added 
# to a worksheet using add_chart() method. 
  
# here we create a line chart object . 
chart1 = workbook.add_chart({'type': 'line'}) 
    
# Add a data series to a chart 
# using add_series method. 
    
# Configure the first series. 
# = Sheet1 !$A$1 is equivalent to ['Sheet1', 0, 0].
  
# note : spaces is not inserted in b / w
# = and Sheet1, Sheet1 and !
# if space is inserted it throws warning.
chart1.add_series({ 
    'name':       '= Sheet1 !$B$1', 
    'categories': '= Sheet1 !$A$2:$A$7', 
    'values':     '= Sheet1 !$B$2:$B$7', 
}) 
    
# Configure a second series. 
# Note use of alternative syntax to define ranges. 
# [sheetname, first_row, first_col, last_row, last_col]. 
chart1.add_series({ 
    'name':       ['Sheet1', 0, 2], 
    'categories': ['Sheet1', 1, 0, 6, 0], 
    'values':     ['Sheet1', 1, 2, 6, 2], 
}) 
    
# Add a chart title  
chart1.set_title ({'name': 'Results of data analysis'}) 
    
# Add x-axis label 
chart1.set_x_axis({'name': 'Test number'}) 
    
# Add y-axis label 
chart1.set_y_axis({'name': 'Data length (mm)'}) 
    
# Set an Excel chart style. 
chart1.set_style(11) 
    
# add chart to the worksheet with given
# offset values at the top-left corner of
# a chart is anchored to cell D2 .  
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10}) 
    
# Finally, close the Excel file  
# via the close() method.  
workbook.close()