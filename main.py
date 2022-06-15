#!/usr/bin/env python3

import sys

ALL_REALMS = ["AA", "AB", "AC", "AD"]

def validate_realm(realm):
    if realm not in ALL_REALMS:
        print(f"Error: realm is absent in {ALL_REALMS}.")
        return False
    return True

def count_sum(sum_list):
    sum_value = sum(sum_list)
    if sum_value > 0:
        return sum_value
    return 0

def main(realm, l):
    if not validate_realm(realm):
        sys.exit(1)

    print(f"Sum of the elements {l} is {count_sum(l)}.")


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8]
    realm = "AB"
    main(realm, l)
