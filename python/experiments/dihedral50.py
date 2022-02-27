from typing import Set
from ..setfamily import SetFamily

d50_mult = [ [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 
      35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49 ], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
      24, 0, 49, 25, 35, 26, 27, 40, 28, 29, 30, 44, 31, 32, 33, 34, 47, 36, 37, 38, 39, 41, 42, 43, 45, 46, 48 ], 
  [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 48, 49, 31, 
      25, 35, 36, 26, 27, 40, 41, 28, 29, 30, 44, 45, 32, 33, 34, 47, 37, 38, 39, 42, 43, 46 ], 
  [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 46, 48, 28, 49, 31, 32, 25, 35, 
      36, 37, 26, 27, 40, 41, 42, 29, 30, 44, 45, 33, 34, 47, 38, 39, 43 ], [ 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
      0, 1, 2, 3, 43, 46, 26, 48, 28, 29, 49, 31, 32, 33, 25, 35, 36, 37, 38, 27, 40, 41, 42, 30, 44, 45, 34, 47, 39 ], 
  [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 39, 43, 
      25, 46, 26, 27, 48, 28, 29, 30, 49, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 47 ], 
  [ 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 47, 39, 49, 43, 25, 35, 46, 26, 
      27, 40, 48, 28, 29, 30, 44, 31, 32, 33, 34, 36, 37, 38, 41, 42, 45 ], [ 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 
      3, 4, 5, 6, 45, 47, 48, 39, 49, 31, 43, 25, 35, 36, 46, 26, 27, 40, 41, 28, 29, 30, 44, 32, 33, 34, 37, 38, 42 ], 
  [ 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 42, 45, 46, 
      47, 48, 28, 39, 49, 31, 32, 43, 25, 35, 36, 37, 26, 27, 40, 41, 29, 30, 44, 33, 34, 38 ], 
  [ 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 38, 42, 43, 45, 46, 26, 47, 48, 
      28, 29, 39, 49, 31, 32, 33, 25, 35, 36, 37, 27, 40, 41, 30, 44, 34 ], [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 
      6, 7, 8, 9, 34, 38, 39, 42, 43, 25, 45, 46, 26, 27, 47, 48, 28, 29, 30, 49, 31, 32, 33, 35, 36, 37, 40, 41, 44 ], 
  [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 44, 34, 47, 
      38, 39, 49, 42, 43, 25, 35, 45, 46, 26, 27, 40, 48, 28, 29, 30, 31, 32, 33, 36, 37, 41 ], 
  [ 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 41, 44, 45, 34, 47, 48, 38, 39, 
      49, 31, 42, 43, 25, 35, 36, 46, 26, 27, 40, 28, 29, 30, 32, 33, 37 ], [ 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
      10, 11, 12, 37, 41, 42, 44, 45, 46, 34, 47, 48, 28, 38, 39, 49, 31, 32, 43, 25, 35, 36, 26, 27, 40, 29, 30, 33 ], 
  [ 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 33, 37, 38, 41, 
      42, 43, 44, 45, 46, 26, 34, 47, 48, 28, 29, 39, 49, 31, 32, 25, 35, 36, 27, 40, 30 ], 
  [ 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 30, 33, 34, 37, 38, 39, 41, 42, 
      43, 25, 44, 45, 46, 26, 27, 47, 48, 28, 29, 49, 31, 32, 35, 36, 40 ], [ 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
      13, 14, 15, 40, 30, 44, 33, 34, 47, 37, 38, 39, 49, 41, 42, 43, 25, 35, 45, 46, 26, 27, 48, 28, 29, 31, 32, 36 ], 
  [ 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 36, 40, 41, 30, 
      44, 45, 33, 34, 47, 48, 37, 38, 39, 49, 31, 42, 43, 25, 35, 46, 26, 27, 28, 29, 32 ], [ 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
      11, 12, 13, 14, 15, 16, 17, 32, 36, 37, 40, 41, 42, 30, 44, 45, 46, 33, 34, 47, 48, 28, 38, 39, 49, 31, 43, 25, 35, 26, 27, 29 ], 
  [ 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 29, 32, 33, 36, 
      37, 38, 40, 41, 42, 43, 30, 44, 45, 46, 26, 34, 47, 48, 28, 39, 49, 31, 25, 35, 27 ], [ 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
      13, 14, 15, 16, 17, 18, 19, 27, 29, 30, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 25, 44, 45, 46, 26, 47, 48, 28, 49, 31, 35 ], 
  [ 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 35, 27, 40, 29, 
      30, 44, 32, 33, 34, 47, 36, 37, 38, 39, 49, 41, 42, 43, 25, 45, 46, 26, 48, 28, 31 ], [ 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
      15, 16, 17, 18, 19, 20, 21, 31, 35, 36, 27, 40, 41, 29, 30, 44, 45, 32, 33, 34, 47, 48, 37, 38, 39, 49, 42, 43, 25, 46, 26, 28 ], 
  [ 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 28, 31, 32, 
      35, 36, 37, 27, 40, 41, 42, 29, 30, 44, 45, 46, 33, 34, 47, 48, 38, 39, 49, 43, 25, 26 ], 
  [ 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 26, 28, 29, 31, 32, 33, 35, 36, 
      37, 38, 27, 40, 41, 42, 43, 30, 44, 45, 46, 34, 47, 48, 39, 49, 25 ], [ 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 
      47, 39, 43, 46, 48, 49, 0, 1, 5, 2, 6, 10, 3, 7, 11, 15, 4, 8, 12, 16, 20, 9, 13, 17, 21, 14, 18, 22, 19, 23, 24 ], 
  [ 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 24, 0, 
      4, 1, 5, 9, 2, 6, 10, 14, 3, 7, 11, 15, 19, 8, 12, 16, 20, 13, 17, 21, 18, 22, 23 ], [ 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 
      43, 46, 48, 49, 25, 26, 28, 31, 35, 20, 21, 0, 22, 1, 5, 23, 2, 6, 10, 24, 3, 7, 11, 15, 4, 8, 12, 16, 9, 13, 17, 14, 18, 19 ], 
  [ 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 23, 24, 3, 0, 4, 8, 1, 5, 9, 13, 2, 6, 10, 14, 
      18, 7, 11, 15, 19, 12, 16, 20, 17, 21, 22 ], [ 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 
      35, 27, 19, 20, 24, 21, 0, 4, 22, 1, 5, 9, 23, 2, 6, 10, 14, 3, 7, 11, 15, 8, 12, 16, 13, 17, 18 ], 
  [ 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 15, 16, 20, 17, 21, 
      0, 18, 22, 1, 5, 19, 23, 2, 6, 10, 24, 3, 7, 11, 4, 8, 12, 9, 13, 14 ], [ 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 
      46, 48, 49, 25, 26, 28, 22, 23, 2, 24, 3, 7, 0, 4, 8, 12, 1, 5, 9, 13, 17, 6, 10, 14, 18, 11, 15, 19, 16, 20, 21 ], 
  [ 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 18, 19, 
      23, 20, 24, 3, 21, 0, 4, 8, 22, 1, 5, 9, 13, 2, 6, 10, 14, 7, 11, 15, 12, 16, 17 ], [ 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 
      28, 31, 35, 27, 29, 32, 36, 40, 30, 14, 15, 19, 16, 20, 24, 17, 21, 0, 4, 18, 22, 1, 5, 9, 23, 2, 6, 10, 3, 7, 11, 8, 12, 13 ], 
  [ 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 10, 11, 15, 12, 16, 20, 13, 17, 21, 0, 14, 18, 22, 
      1, 5, 19, 23, 2, 6, 24, 3, 7, 4, 8, 9 ], [ 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 
      25, 26, 28, 31, 21, 22, 1, 23, 2, 6, 24, 3, 7, 11, 0, 4, 8, 12, 16, 5, 9, 13, 17, 10, 14, 18, 15, 19, 20 ], 
  [ 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 17, 18, 22, 19, 23, 2, 20, 24, 
      3, 7, 21, 0, 4, 8, 12, 1, 5, 9, 13, 6, 10, 14, 11, 15, 16 ], [ 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 
      40, 30, 33, 13, 14, 18, 15, 19, 23, 16, 20, 24, 3, 17, 21, 0, 4, 8, 22, 1, 5, 9, 2, 6, 10, 7, 11, 12 ], 
  [ 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 9, 10, 
      14, 11, 15, 19, 12, 16, 20, 24, 13, 17, 21, 0, 4, 18, 22, 1, 5, 23, 2, 6, 3, 7, 8 ], [ 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 
      33, 37, 41, 44, 34, 38, 42, 45, 47, 5, 6, 10, 7, 11, 15, 8, 12, 16, 20, 9, 13, 17, 21, 0, 14, 18, 22, 1, 19, 23, 2, 24, 3, 4 ], 
  [ 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 16, 17, 21, 18, 22, 1, 19, 23, 2, 6, 20, 24, 3, 7, 
      11, 0, 4, 8, 12, 5, 9, 13, 10, 14, 15 ], [ 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 
      30, 33, 37, 12, 13, 17, 14, 18, 22, 15, 19, 23, 2, 16, 20, 24, 3, 7, 21, 0, 4, 8, 1, 5, 9, 6, 10, 11 ], 
  [ 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 8, 9, 13, 10, 14, 18, 11, 
      15, 19, 23, 12, 16, 20, 24, 3, 17, 21, 0, 4, 22, 1, 5, 2, 6, 7 ], [ 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 
      38, 42, 45, 47, 39, 4, 5, 9, 6, 10, 14, 7, 11, 15, 19, 8, 12, 16, 20, 24, 13, 17, 21, 0, 18, 22, 1, 23, 2, 3 ], 
  [ 44, 34, 38, 42, 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 11, 12, 
      16, 13, 17, 21, 14, 18, 22, 1, 15, 19, 23, 2, 6, 20, 24, 3, 7, 0, 4, 8, 5, 9, 10 ], [ 45, 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 
      40, 30, 33, 37, 41, 44, 34, 38, 42, 7, 8, 12, 9, 13, 17, 10, 14, 18, 22, 11, 15, 19, 23, 2, 16, 20, 24, 3, 21, 0, 4, 1, 5, 6 ], 
  [ 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 3, 4, 8, 5, 9, 13, 6, 10, 14, 18, 7, 11, 15, 19, 
      23, 12, 16, 20, 24, 17, 21, 0, 22, 1, 2 ], [ 47, 39, 43, 46, 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 
      42, 45, 6, 7, 11, 8, 12, 16, 9, 13, 17, 21, 10, 14, 18, 22, 1, 15, 19, 23, 2, 20, 24, 3, 0, 4, 5 ], 
  [ 48, 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 45, 47, 39, 43, 46, 2, 3, 7, 4, 8, 12, 
      5, 9, 13, 17, 6, 10, 14, 18, 22, 11, 15, 19, 23, 16, 20, 24, 21, 0, 1 ], [ 49, 25, 26, 28, 31, 35, 27, 29, 32, 36, 40, 30, 33, 37, 41, 44, 34, 38, 42, 
      45, 47, 39, 43, 46, 48, 1, 2, 6, 3, 7, 11, 4, 8, 12, 16, 5, 9, 13, 17, 21, 10, 14, 18, 22, 15, 19, 23, 20, 24, 0 ] ]

d10_mult = [ [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [ 1, 2, 3, 4, 0, 9, 5, 6, 7, 8 ], [ 2, 3, 4, 0, 1, 8, 9, 5, 6, 7 ], 
  [ 3, 4, 0, 1, 2, 7, 8, 9, 5, 6 ], [ 4, 0, 1, 2, 3, 6, 7, 8, 9, 5 ], [ 5, 6, 7, 8, 9, 0, 1, 2, 3, 4 ], 
  [ 6, 7, 8, 9, 5, 4, 0, 1, 2, 3 ], [ 7, 8, 9, 5, 6, 3, 4, 0, 1, 2 ], [ 8, 9, 5, 6, 7, 2, 3, 4, 0, 1 ], 
  [ 9, 5, 6, 7, 8, 1, 2, 3, 4, 0 ] ]

d50_names = ["e", "\\alpha"]
for i in range(2, 25):
    d50_names.append("\\alpha^{" + str(i) + "}")

d50_names.append("\\beta")
lookup = [ 27, 29, 32, 36, 28, 30, 33, 37, 41, 31, 34, 38, 42, 45, 35, 39, 43, 46, 48, 40, 44, 47, 49, 50 ]
for i in range(26, 50):
    power = lookup.index(i+1)+1
    if power == 1:
        d50_names.append("\\beta\\alpha")
    else:
        d50_names.append("\\beta\\alpha^{" + str(power) + "}")

print(d50_names)

d50_sets = [ [ 0, 1, 2, 3, 25, 26, 28 ], [ 7, 14, 21, 30, 31, 42, 49 ] ]

d50_edf = SetFamily(d50_sets, d50_mult, elstr=d50_names)
print([[d50_names[x] for x in s] for s in d50_sets])
#d50_edf.print_external_differences(sort_by="value", perline=5)
print(d50_edf.is_edf())
print(d50_edf.is_sedf())

d50_edf.print_external_differences_tables()
print("----")
d50_im_sets = [ [ 0, 5, 1, 6, 2, 7, 3 ], [ 5, 1, 2, 7, 8, 4, 9 ] ]
d10_names = [
    "e",
    "\\alpha^2",
    "\\beta",
    "\\beta\\alpha",
    "\\alpha^4",
    "\\alpha",
    "\\alpha^3",
    "\\beta\\alpha^2",
    "\\beta\\alpha^3",
    "\\beta\\alpha^4",
]

d50_im = SetFamily(d50_im_sets, d10_mult, elstr=d10_names)
[[print(d10_names[x], end=", ") for x in s] for s in d50_im_sets]
print(d50_im.is_edf())
print(d50_im.is_sedf())

d50_im.print_external_differences_tables()