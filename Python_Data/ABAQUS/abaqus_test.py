# Collection of testing string from ABAQUS inp files

testNSet = """*Heading
** Job name: nlBuckle_basic Model name: Model-2_NL
** Generated by: Abaqus/CAE 6.14-2
*Preprint, echo=YES, model=YES, history=YES, contact=YES
**
*Node
      1,  -914.400024,          -10.,           0.
      2,   914.400024,   25.3999996,           0.
      3,   914.400024,   50.7999992,           0.
      4,   914.400024,   76.1999969,           0.
      5,   914.400024,   101.599998,           0.
*Elset, elset=Set_botPl_s2_w2, generate
 1916,  2023,     1
** Section: endPl_t
*Shell Section, elset=Set_endPl_w, material=astmA36, offset=SNEG
38.1, 5
** Section: endPl_t
*Shell Section, elset=Set_endPl_s, material=astmA36, offset=SNEG
38.1, 5
** Section: SidePlusTransCap
*Shell Section, elset=Set_transCap_w, material=astmA36, offset=SNEG
28.575, 5
** Section: SidePlusTransCap
*Shell Section, elset=Set_transCap_e, material=astmA36, offset=SNEG
28.575, 5
** Section: transS_w
*Shell Section, elset=Set_transStiff_W, material=astmA36
6.096, 5
** Section: transS_f
*Shell Section, elset=Set_transStiff_F, material=astmA36
8.382, 5
** Section: longG_f
*Shell Section, elset=Set_longGir_F, material=astmA36, offset=1.2
8.89, 5
** Section: longG_w
*Shell Section, elset=Set_longGir_W, material=astmA36_NL_kine
5.97, 5
** Section: sidePl_t
*Shell Section, elset=Set_sidePl_w, material=astmA36, offset=SNEG
9.525, 5
** Section: sidePl_t
*Shell Section, elset=Set_sidePl_e, material=astmA36, offset=SNEG
9.525, 5
** Section: botPlB
*Shell Section, elset=Set_botPl_B, material=astmA36_NL_iso, offset=0.5
6.35, 5
** Section: longS_f
*Shell Section, elset=Set_longStiff_F, material=astmA36
5.715, 5
** Section: botPlA
*Shell Section, elset=Set_botPl_A, material=astmA36, offset=SPOS
7.938, 5
** Section: longS_w
*Shell Section, elset=Set_longStiff_W, material=astmA36
5.08, 5
*End Assembly"""

testNode = """
*Node
      1,  -914.400024,          -10.,           0.
      2,   914.400024,   25.3999996,           0.
      3,   914.400024,   50.7999992,           0.
      4,   914.400024,   76.1999969,           0.
      5,   914.400024,   101.599998,           0.
      6,   914.400024,         127.,           0.
      7,   914.400024,   152.399994,           0.
      8,   914.400024,   177.800003,           0.
      9,   914.400024,   203.199997,           0.
     10,   914.400024,   228.600006,           0.
"""

testString = """
*Heading
** Job name: nlBuckle_basic Model name: Model-2_NL
** Generated by: Abaqus/CAE 6.14-2
*Preprint, echo=YES, model=YES, history=YES, contact=YES
**
** PARTS
**
*Part, name=grillage
*Node
      1,   914.400024,           0.,           0.
      2,   914.400024,   25.3999996,           0.
      3,   914.400024,   50.7999992,           0.
      4,   914.400024,   76.1999969,           0.
      5,   914.400024,   101.599998,           0.
      6,   914.400024,         127.,           0.
      7,   914.400024,   152.399994,           0.
      8,   914.400024,   177.800003,           0.
      9,   914.400024,   203.199997,           0.
     10,   914.400024,   228.600006,           0.
     11,   914.400024,        -254.,           0.
     12,   914.400024,   279.399994,           0.
     13,   914.400024,   304.799988,           0.
     14,         889.,           0.,           0.
     15,    889.05719,   25.3999996,           0.
     16,   889.114441,   50.7999992,           0.
     17,   889.171631,   76.1999969,           0.
     18,   889.228821,   101.599998,           0.
     19,   889.286011,         127.,           0.
     20,   889.343262,   152.399994,           0.
*Element, type=S4R-1
  1,   1,   2,  15,  14
  2,   2,   3,  16,  15
  3,   3,   4,  17,  16
  4,   4,   5,  18,  17
  5,   5,   6,  19,  18
*Elset, elset=Set_transStiff_W
 40728, 40729, 40730, 40731, 40732, 40733, 40734, 40735, 40736, 40737, 40738, 40739, 40740, 40741, 40742, 40743
 40744, 40745, 40746, 40747, 40748, 40749, 40750, 40751, 40752, 40753, 40754, 40755, 40756, 40757, 40758, 40759
*Nset, nset=Set_transStiff_F
 28530, 28599, 28749, 28910, 28979, 29018, 31207, 31209, 31219, 31222, 31252, 31446, 31727, 31745, 31754, 31765
 31789, 31816, 31843, 32325, 41161, 41162, 41163, 41164, 41165, 41166, 41167, 41168, 41169, 41170, 41175, 41176
*Elset, elset=Set_botPl_A, generate
 12865,  28128,      1
*Assembly, name=Assembly
** Section: botPlB
*Shell Section, elset=Set_botPl_B, material=astmA36, offset=SPOS
6.35, 5
** Section: botPlA
*Shell Section, elset=Set_botPl_A, material=astmA36, offset=SPOS
7.938, 5
*End Assembly"""
