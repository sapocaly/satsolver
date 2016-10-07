#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
@version: ??
@author: Ye Sheng
@license: Apache Licence
@contact: sym1all@hotmail.com
@file: main
@time: 10/5/16 8:38 PM
@project: SATsolver
"""

import solvers
import os

path = "../file/A3Formulas"

for filename in os.listdir(path):
    solvers.calls = 0
    fin = open("../file/A3Formulas/" + filename, 'r')
    lines = fin.readlines()
    conf = lines[1]
    lines = lines[2:]
    clauses = []
    count = int(conf.split()[2])
    partial = [-1 for i in range(count + 1)]
    for line in lines:
        line = map(int, line[:-1].split()[:-1])
        clauses.append(line)
    res1,res2 = solvers.WALKSAT(clauses, partial)
    print filename, ',',res1,',',res2,',',solvers.DPLL(clauses,partial)!=False,',',solvers.calls
