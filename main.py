# CS5001 HW2
# Ben Simpson
# 12-12-2018

def printValues(values):
   print('+-------+-------+-------+-------+-------+-------+-------+-------+')
   for i in values:
        print('|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
   print('+-------+-------+-------+-------+-------+-------+-------+-------+\n')

def main():
    values = [i for i in range(10)]
    printValues(values)
    return

if __name__ = '__main__':
    main()