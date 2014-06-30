#!/usr/bin/env python
'''
Created on Jul 24, 2013

@author: Kevin Evans
@note: The requirement from the email stated an "array of
characters" should be passed to the function so I have 
intentionally used the array type rather than a list. The
resulting code is slightly more complicated but has better
performance and memory usage.
'''

import string
import array

def letterFlip(alphaArray):
    '''
    @summary: function used to reverse an array of letters and 
    change the vowels to uppercase.
    @param: alphaArray type: array.array('c') character array
    @rtype: array.array('c')
    '''
    alphaArray.reverse()
    #change the vowels in place to save space
    for idx in range(len(alphaArray)):
        #is it a vowel
        if alphaArray[idx] in 'aeiou':
            alphaArray[idx] = alphaArray[idx].upper()
    return alphaArray
            
def main():
    #initialize the array as a character array
    letterArray = array.array('c')
    letterArray.fromstring(string.lowercase)
    print 'Input: ' + letterArray.tostring()
    flippedList = letterFlip(letterArray)
    print 'Output: ' + flippedList.tostring()

if __name__ == '__main__':
    main()       
