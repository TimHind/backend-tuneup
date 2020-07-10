#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    
    
  
    # sortby = SortKey.CUMULATIVE
    # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # ps.print_stats()
    # print(s.getvalue())
    @functools.wraps(func)
    def inner(*args, **kwargs):
        pf = cProfile.Profile()
        pf.enable()
        result = func(*args, **kwargs)
        pf.disable()
        ps = pstats.Stats(pf).sort_stats("cumulative")
        ps.print_stats(10)
        return result
    return inner


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    movie = movies.pop()
    if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt="find_duplicate_movies('movies.txt')", setup="from __main__ import find_duplicate_movies")
    result = t.repeat(repeat=7, number=5)
    exact_time = min(result) / float(5)
    return "Best time across 7 repeats of 5 runs per repeat: " + str(exact_time)


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    print(timeit_helper())


if __name__ == '__main__':
    main()
