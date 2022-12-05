#!/usr/bin/python3
if __name__ == "__main__":
    def add_tuple(tuple_a=(), tuple_b=()):

        sum_tup = ()
        if len(tuple_b) < 2:
            while len(tuple_b) < 2:
                tuple_b += 0,
        if len(tuple_a) < 2:
            while len(tuple_a) < 2:
                tuple_a += 0,
        for i in range(2):
            sum_tup += tuple_a[i] + tuple_b[i],
        return sum_tup
