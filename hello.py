# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:55:07 2017

@author: dlf4mf
"""

import helper
from calculator import add

def main():
    helper.greeting("hello")
    result = add(1, 7)
    helper.greeting(result)
    
if __name__ == "__main__":
    main()