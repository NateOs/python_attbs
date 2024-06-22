tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

# Calculate the maximum length of each column
column_widths = [max(len(row[i]) 
    for row in tableData)
        for i in range(len(tableData[0]))]

# Iterate through each row and print elements from each column, adjusting to the right
for row in tableData:
    for i in range(len(row)):
        print(row[i].rjust(column_widths[i]), end=' ')
    print()  # Move to the next line after each row
