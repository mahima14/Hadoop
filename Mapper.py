import sys
import line as line


def mapper():
    f = open('output.txt', 'w')

    for line in sys.stdin:
        data = line.strip().split("\t")
      #  print data
        date, time, store, item, cost, payment = data
       # print data
        input = "{0}\t{1}".format(item, cost)
        print input
        f.write(input())
        #print >> f, 'Filename:', input  # or f.write('...\n')
    f.close()
        #print sys.stdout.read()

test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard"""

# This function allows you to test the mapper with the provided test string
if __name__ == "__main__":

    f = open('purchases.txt', 'r+')
    line = f.read()
    print line
    mapper()
#sys.stdin = StringIO.StringIO(test_text)

	#sys.stdin = sys.__stdin__
