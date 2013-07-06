import sys
from datetime import datetime
import requests
import itertools


if __name__ == '__main__':
    date_format = '%Y-%m-%dT%H:%M:%S'
    last_date = None

    def calc_dates():
        for i in itertools.chain(requests.get(sys.argv[1]).iter_lines()):
            date1, date2 = [datetime.strptime(k, date_format) for k in i.split(',')]
            yield abs(date2 - date1).total_seconds()

    #print "{:f}".format(sum(calc_dates()) + 23)

    def calc_empty_pixels():
        fd = open(sys.argv[1], 'rb')

        def isprime(n):
            """check if integer n is a prime"""
            # range starts with 2 and only needs to go up the squareroot of n
            if n < 2:
                return False
            for x in xrange(2, int(n ** 0.5) + 1):
                if n % x == 0:
                    return False
            return True

        for c in fd.read():
            if isprime(ord(c)):
                yield 1

    # print sum(calc_empty_pixels())

    # $('input[name="answer"]').val(eval($('#math').text())); $('form').submit();
