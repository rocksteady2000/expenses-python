#!/usr/bin/python
import csv
import statistics
import sys
"""
this program takes csv containing monthly expenses
from given csv containing monthly expenses per category line item and 
calculates the average monthly cost of an expense per category.
Also calculates the average monthly overall cost.
"""

class SpecialIndexWarning(UserWarning):
        OutofRangeWarning = 'Out of Range --pls make sure all values are listed in appropriate columns. This program will only process data within 12 columns for each month.'

def main():
    usage = 'Usage: python3 expenses.py <filepath>'
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1],'r') as fp:
                data = csv.reader(fp, delimiter=',')
                aveSum=0
                for row in data:
                    try:
                        if len(row)>13: #custom warning when values are entered in extraneous columns
                            print(SpecialIndexWarning.OutofRangeWarning)
                            row = row[:13] #truncate list to only parse values for each month
                        #pull out expense category from each row
                        category = row.pop(0)
                        #calculate average monthly cost for each line item
                        ave = statistics.mean(float(x) for x in row)
                        #print(ave)
                        #tally all averages to get total sum
                        aveSum += ave
                        print('average monthly cost for {0} is ${1:.2f}'.format(category,ave))
                        #exception handling if string entered instead of int/float in any field

                    except ValueError as err: # process ValueError only
                        if (category[:2] =='//' or category[:2]=='/*' or category=='expense'): #ignore header row and comment rows
                            del row
                        else:
                            print('Please make sure values contain numbers only and no symbols nor characters. This row is skipped: Row:{}; Reason :{}'.format(category, err) )
                        continue
                    except IndexError as err:
                        if len(row) ==0:
                            print('Skipping empty row. Reason : {}',err)
                #display final tally of sum of all averages
                print('The total average monthly expenses is ${0:.2f}'.format(aveSum))
        except TypeError as err:
            print('type error',err)
        except FileNotFoundError as err:
            print('Incorrect file or path. Please try again!',err)
        except csv.Error as e:
            sys.exit('Please use properly formatted csv!  file {}, line {}: {}'.format(sys.argv[1], data.line_num, e))
        except ValueError as e:
            print('value error:', e)

            fp.close()
    else:
        print('Inccorrect command. You entered', str(sys.argv), 'Need to enter one filename for input into program. ',usage)
if __name__ == "__main__":
    sys.exit(main())
