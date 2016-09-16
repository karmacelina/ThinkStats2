"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file = '2002FemResp.dct',
                dat_file = '2002FemResp.dat.gz'):
    """ Reads NSFG respondent data. 

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """

    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression = 'gzip')
    return df

def Validate(df):

    preg = nsfg.ReadFemPreg()

    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in df.pregnum.iteritems():
        caseid = df.caseid[index]
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()
    print(resp.shape)

    assert resp.caseid[2] == 11586
    assert Validate(resp) == True

    print(resp.pregnum.value_counts().sort_index())
    print("7 or more pregnancies: %d" % len(resp[resp.pregnum >= 7]))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
