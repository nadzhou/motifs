#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:39:33 2022

@author: student
"""
import pandas as pd
import itertools
import re

def main():
    file = "data_seq.txt"
    freq_file = 'threshold_frequency.csv'
    resid_col = 'Neighbouring_residues'

    data = read_file(file)
    # print(data)
    df = pd.read_csv(freq_file)
    patterns = df[resid_col].tolist()
    found = find_pattern(data, patterns)

    print(set(found))


def read_file(dir):
    with open(dir, "r") as file:
        data = file.read().split()

    data = [pat for pat in data if len(pat) == 9]
    return data


def find_pattern(total_list, pattern_list):
    found = []
    for motif in total_list:
        for three_comb in itertools.combinations(pattern_list, 3):
            # three_comb = ''.join(three_comb)
            result = re.findall(rf'({three_comb[0]}).?{three_comb[1]}.?{three_comb[2]}', motif)
            if len(result) > 1:
                print(result)

    return found


if __name__ == "__main__":
    main()
     