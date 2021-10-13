import pandas as pd

'''
When making a dataframe with a dict in pandas the keys become the columns and the values become the rows
'''
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test1', 'Test2', 'Test3']

'''
.T method transposes the rows and columns and switches them, its not permanent
'''
# print(grades.T)
# print(grades)
# print(grades['Eva'])
# print(grades.Sam)

'''
using loc and iloc methods
'''
# print(grades.loc['Test2'])
# print(grades.iloc[1])

'''
For consecutive rows
'''
# print(grades.loc['Test1':'Test3'])
# print(grades.iloc[0:3])

'''
For non consecutive rows
'''
#print(grades.loc[['Test1', 'Test3']])
#print(grades.iloc[[0, 2]])

'''
Viewing only Eva's and Katie's grades for Test1 and Test 2
'''
#print(grades.loc[:':Test2', ['Eva', 'Katie']])

'''
View only Sam's THRU Bob's grades for Test1 and Test2
'''
#print(grades.loc[['Test1', 'Test3'], 'Sam':'Bob'])

'''
Getting everone with an A grade
'''
grades_A = grades[grades >= 90]
# print(grades_A)

'''
Getting everyone with a B grade
'''
grades_B = grades[(grades >= 80) & (grades < 90)]

'''
Creating a dataframe for everone with an A or B
'''
grades_A_or_B = [(grades >= 90) | (grades >= 80)]
# print(grades_A_or_B)

'''
Used .t to get a description of the Tests which is the rows
Set it to only show 2 decimal points
'''
pd.set_option('precision', 2)
# print(grades.T.describe())

'''
Different ways to Sort
'''
print(grades.sort_index(ascending=False))
print(grades.sort_index(axis=1, ascending=False))
print(grades.sort_values(by='Test1', axis=1, ascending=False))
print(grades.T.sort_values(by='Test1', ascending=False))
print(grades.loc['Test1'].sort_values(ascending=False))
