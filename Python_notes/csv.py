# import _csv
import _csv
# with open('data2.csv') as file:
#     read = _csv.read(file)
#
#     count = 0
#
#     for row in read:
#         print(row[3])
#         if count>5:
#             break
#         count+=1
#

with open('mycsv1.csv','w',newline='') as f:
    wright = _csv.writer(f)

    wright.writerow(['col','col1','cal2'])
    wright.writerow(['col', 'col1', 'cal2'])



