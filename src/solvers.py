#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
@version: ??
@author: Ye Sheng
@license: Apache Licence
@contact: sym1all@hotmail.com
@file: DPLL
@time: 10/5/16 7:02 PM
@project: SATsolver
"""
import random

Undefined = -1


def evaluate(clause, model):
    # return "True" if some literal is True
    # return  "False" if all literals are False
    # otherwise, undifined, return undefined literal count
    undefined = 0
    for literal in clause:
        if model[abs(literal)] == -1:
            undefined += 1
        elif model[abs(literal)] == (literal > 0):
            return "True"
    if undefined == 0:
        return "False"
    return undefined




def evaluate_all_clauses(clauses, model):
    undefined = 0
    ress = []
    for clause in clauses:
        res = evaluate(clause, model)
        ress.append(res)
        if res == "False":
            return "False"
        elif res != "True":
            undefined += 1
    if undefined == 0:
        return "True"
    return ress

calls = 0

def DPLL(clauses, partial_valuation, depth=0):
    global calls
    calls += 1
    ress = evaluate_all_clauses(clauses, partial_valuation)
    if ress == "True":
        return partial_valuation
    elif ress == "False":
        return False
    else:
        for i in range(len(ress)):
            if ress[i] == 1:
                if len(clauses[i]) == 1:
                    partial_valuation[abs(clauses[i][0])] = clauses[i][0] > 0
                    ans = DPLL(clauses, partial_valuation, depth + 1)
                    if not ans:
                        partial_valuation[abs(clauses[i][0])] = -1
                    return ans
        for i in range(len(ress)):
            if ress[i] == 1:
                for literal in clauses[i]:
                    if partial_valuation[abs(literal)] == -1:
                        partial_valuation[abs(literal)] = literal > 0
                        ans = DPLL(clauses, partial_valuation, depth + 1)
                        if not ans:
                            partial_valuation[abs(literal)] = -1
                        return ans
        for i in range(1, len(partial_valuation)):
            if partial_valuation[i] == -1:
                partial_valuation[i] = False
                if DPLL(clauses, partial_valuation, depth + 1):
                    return partial_valuation
                else:
                    partial_valuation[i] = True
                    ans = DPLL(clauses, partial_valuation, depth + 1)
                    if not ans:
                        partial_valuation[i] = -1
                    return ans


def get_unsatisfied(clauses, partial_valuation):
    unsatisfied = []
    for clause in clauses:
        res = evaluate(clause, partial_valuation)
        if res != "True":
            unsatisfied.append(clause)
    return unsatisfied

def WALKSAT(clauses, partial_valuation):
    current_best = 0
    for i in range(9012):
        unsatisfied = get_unsatisfied(clauses, partial_valuation)
        if not unsatisfied:
            return True, i
        random.shuffle(unsatisfied)
        clause = unsatisfied[0]
        best = len(clauses)
        for l in clause:
            v = partial_valuation[:]
            v[abs(l)] = l > 0
            unst = get_unsatisfied(clauses, v)
            if len(unst) < best:
                best = len(unst)
                bestv = v
        partial_valuation = bestv
        if best < current_best:
            current_best = best
    return len(clauses) - current_best,i

