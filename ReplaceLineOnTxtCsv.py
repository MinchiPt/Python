with open('/Users/magnetosa/Python/rcs/merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open('/Users/magnetosa/Python/rcs/merged.csv', 'w') as file:
  file.writelines(content) # writeline works with lists, if you want to use write then you'll have to convert content[0] to string
