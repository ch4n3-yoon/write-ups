#!/usr/bin/python
# coding: utf-8

from pwn import *
from z3 import *

p = remote('52.79.210.195', 9999)

op1 = Int('op1')
op2 = Int('op2')
op3 = Int('op3')
op4 = Int('op4')
op5 = Int('op5')
op6 = Int('op6')
op7 = Int('op7')
op8 = Int('op8')
op9 = Int('op9')
op10 = Int('op10')
op11 = Int('op11')
op12 = Int('op12')
op13 = Int('op13')
op14 = Int('op14')
op15 = Int('op15')

s = Solver()

s.add((102 * (104 + op1)) + (505 * (500 + op2)) + (423 *(400 + op3)) \
    + (20 * (23 + op4)) + (63 * (72 + op5)) + (30 * (15 + op6)) \
    + (1001 * (404 + op7)) + (666 * (3 + op8)) + (423 * (98 + op9)) \
    + (57 * (20 + op10)) + (2 * (94 + op11)) + (41 * (32 + op12)) \
    + (27 * (53 + op13)) + (432 * (9 + op14)) + (53 * (50 + op15)) == 2827917)

s.add((511 * (523 + op1)) + (520 * (53 + op2)) + (513 * (554 + op3)) \
    + (524 * (565 + op4)) + (555 * (546 + op5)) + (576 * (507 + op6)) \
    + (57 * (58 + op7)) + (538 * (59 + op8)) + (59 * (60 + op9)) \
    + (601 * (610 + op10)) + (621 * (652 + op11)) + (632 * (623 + op12)) \
    + (630 * (641 + op13)) + (644 * (65 + op14)) + (605 * (616 + op15)) == 7909983)

s.add((42 * (345 + op1)) + (192 * (582 + op2)) + (952 * (734 + op3)) \
    + (11 * (12 + op4)) + (93 * (43 + op5)) + (96 * (254 + op6)) \
    + (43 * (88 + op7)) + (34 * (64 + op8)) + (23 * (256 + op9)) \
    + (85 * (723 + op10)) + (10 * (53 + op11)) + (504 * (102 + op12)) \
    + (690 * (108 + op13)) + (32 * (7 + op14)) + (88 * (94 + op15)) == 3161706)
# Equation 4
s.add((41 * (45 + op1)) + (12 * (52 + op2)) + (52 * (73 + op3)) \
    + (110 * (120 + op4)) + (903 * (403 + op5)) + (946 * (24 + op6)) \
    + (13 * (55 + op7)) + (32 * (12 + op8)) + (89 * (25 + op9)) \
    + (52 * (20 + op10)) + (12 * (89 + op11)) + (956 * (534 + op12)) \
    + (52 * (28 + op13)) + (2 * (98 + op14)) + (17 * (15 + op15)) == 3277498 )



# Equation 5
s.add( (12 * (48 + op1)) + (7 * (5 + op2)) + (3 * (6 + op3)) \
    + (52 * (34 + op4)) + (78 * (76 + op5)) + (52 * (64 + op6)) \
    + (30 * (50 + op7)) + (53 * (38 + op8)) + (77 * (74 + op9)) \
    + (234 * (432 + op10)) + (123 * (321 + op11)) + (889 * (998 + op12)) \
    + (58 * (93 + op13)) + (734 * (295 + op14)) + (941 * (953 + op15)) == 3611263 )



# Equation 6
s.add( (38 * (10 + op1)) + (92 * (74 + op2)) + (35 * (7 + op3)) \
    + (83 * (95 + op4)) + (39 * (18 + op5)) + (25 * (85 + op6)) \
    + (77 * (43 + op7)) + (83 * (75 + op8)) + (54 * (34 + op9)) \
    + (90 * (770 + op10)) + (999 * (888 + op11)) + (344 * (544 + op12)) \
    + (14 * (33 + op13)) + (888 * (777 + op14)) + (666 * (543 + op15)) == 3837898 )



# Equation 7
s.add( (111 * (123 + op1)) + (22 * (34 + op2)) + (222 * (234 + op3)) \
    + (33 * (45 + op4)) + (333 * (345 + op5)) + (44 * (45 + op6)) \
    + (444 * (456 + op7)) + (55 * (56 + op8)) + (555 * (567 + op9)) \
    + (66 * (67 + op10)) + (666 * (678 + op11)) + (77 * (78 + op12)) \
    + (777 * (789 + op13)) + (88 * (89 + op14)) + (888 * (890 + op15)) == 5188642)



# Equation 8
s.add( (1 * (3 + op1)) + (2 * (4 + op2)) + (3 * (5 + op3)) \
    + (4 * (6 + op4)) + (5 * (7 + op5)) + (6 * (8 + op6)) \
    + (7 * (9 + op7)) + (8 * (1 + op8)) + (9 * (2 + op9)) \
    + (1 * (5 + op10)) + (2 * (6 + op11)) + (3 * (7 + op12)) \
    + (4 * (8 + op13)) + (5 * (9 + op14)) + (6 * (6 + op15)) == 37650 )



# Equation 9
s.add( (321 * (313 + op1)) + (432 * (424 + op2)) + (543 * (535 + op3)) \
    + (654 * (646 + op4)) + (765 * (757 + op5)) + (876 * (868 + op6)) \
    + (987 * (979 + op7)) + (109 * (101 + op8)) + (210 * (202 + op9)) \
    + (321 * (323 + op10)) + (432 * (434 + op11)) + (543 * (545 + op12)) \
    + (654 * (656 + op13)) + (765 * (767 + op14)) + (876 * (878 + op15)) == 11019161 )



# Equation 10
s.add( (74 * (396 + op1)) + (102 * (452 + op2)) + (942 * (592 + op3)) \
    + (125 * (692 + op4)) + (932 * (954 + op5)) + (194 * (205 + op6)) \
    + (693 * (104 + op7)) + (304 * (502 + op8)) + (237 * (349 + op9)) \
    + (289 * (169 + op10)) + (590 * (902 + op11)) + (451 * (893 + op12)) \
    + (758 * (934 + op13)) + (402 * (806 + op14)) + (323 * (490 + op15)) == 8423859 )



# Equation 11
s.add( (84 * (39 + op1)) + (29 * (44 + op2)) + (20 * (594 + op3)) \
    + (124 * (50 + op4)) + (973 * (4 + op5)) + (192 * (273 + op6)) \
    + (599 * (47 + op7)) + (32 * (598 + op8)) + (290 * (100 + op9)) \
    + (66 * (823 + op10)) + (4 * (832 + op11)) + (9 * (178 + op12)) \
    + (909 * (32 + op13)) + (483 * (778 + op14)) + (203 * (223 + op15)) == 3464901 )



# Equation 12
s.add( (100 * (349 + op1)) + (89 * (595 + op2)) + (299 * (312 + op3)) \
    + (290 * (707 + op4)) + (28 * (38 + op5)) + (76 * (64 + op6)) \
    + (667 * (500 + op7)) + (490 * (588 + op8)) + (644 * (34 + op9)) \
    + (857 * (823 + op10)) + (85 * (902 + op11)) + (302 * (543 + op12)) \
    + (871 * (402 + op13)) + (336 * (495 + op14)) + (986 * (255 + op15)) == 6377985 )



# Equation 13
s.add( (70 * (96 + op1)) + (12 * (52 + op2)) + (94 * (59 + op3)) \
    + (12 * (69 + op4)) + (93 * (95 + op5)) + (19 * (20 + op6)) \
    + (69 * (10 + op7)) + (30 * (50 + op8)) + (23 * (34 + op9)) \
    + (28 * (16 + op10)) + (59 * (90 + op11)) + (45 * (89 + op12)) \
    + (75 * (93 + op13)) + (40 * (80 + op14)) + (32 * (49 + op15)) == 480427 )



# Equation 14
s.add( (74 * (396 + op1)) + (102 * (452 + op2)) + (942 * (592 + op3)) \
    + (125 * (692 + op4)) + (932 * (954 + op5)) + (194 * (205 + op6)) \
    + (693 * (104 + op7)) + (304 * (502 + op8)) + (237 * (349 + op9)) \
    + (289 * (169 + op10)) + (590 * (902 + op11)) + (451 * (893 + op12)) \
    + (758 * (934 + op13)) + (402 * (806 + op14)) + (323 * (490 + op15)) == 8423859 )



# Eqiatopm 15
s.add( (95 * (82 + op1)) + (47 * (862 + op2)) + (33 * (51 + op3)) \
    + (909 * (64 + op4)) + (66 * (13 + op5)) + (84 * (72 + op6)) \
    + (78 * (99 + op7)) + (53 * (24 + op8)) + (70 * (37 + op9)) \
    + (64 * (21 + op10)) + (20 * (39 + op11)) + (50 * (18 + op12)) \
    + (17 * (98 + op13)) + (309 * (301 + op14)) + (73 * (95 + op15)) == 1488651 )

s.add(op1>0, op2>0, op3>0, op4>0)
s.check()
print s.model()

ops = s.model()

for i in range(1, 16):
    print p.recv(1024)
    eval('p.sendline(str(ops[op{0}]))'.format(i))
print p.recv(1024)
