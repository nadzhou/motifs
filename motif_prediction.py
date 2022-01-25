#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:39:33 2022

@author: student
"""
import pandas as pd
import itertools


def main():
    file = "data_seq.txt"
    freq_file = 'threshold_frequency.csv'
    resid_col = 'Neighbouring_residues'
    out_file = 'fixed.txt'

    data = read_file(file)
    df = pd.read_csv(freq_file)
    patterns = df[resid_col].tolist()
    found = find_pattern(data, patterns)
    if len(found) > 1:
        write_to_file(found, out_file)
        print(f"Motifs written to file: {out_file}")
    else:
        print("No tmoifs found.")


def write_to_file(data, dir):
    with open(dir, "w") as file:
        for line in data:
            print(line, file=file)


def read_file(dir):
    with open(dir, "r") as file:
        data = file.read().split()

    data = [pat for pat in data if len(pat) == 9]
    return data


def find_pattern(total_list, pattern_list):
    found = []
    for motif in total_list:
        for three_comb in itertools.combinations(pattern_list, 3):
            first_comb, second_comb, third_comb = three_comb
            if first_comb in motif and second_comb in motif and third_comb in motif:
                found.append(motif)
    return set(found)


if __name__ == "__main__":
    main()
