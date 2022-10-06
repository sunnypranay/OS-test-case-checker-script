#!/bin/bash
gcc wis-grep.c
./a.out > ./program-output/program-output-wis-grep-1.txt
./a.out hello random.txt> ./program-output/program-output-wis-grep-2.txt
./a.out hello testcase-1.txt> ./program-output/program-output-wis-grep-3.txt
./a.out hello testcase-1.txt testcase-2.txt > ./program-output/program-output-wis-grep-4.txt
gcc wis-tar.c
./a.out > ./program-output/program-output-wis-tar-1.txt
./a.out test.tar testcase-4.txt testcase-3.txt > ./program-output/program-output-wis-tar-2.txt
./a.out test.tar testcase-1.txt testcase-2.txt > ./program-output/program-output-wis-tar-3.txt
rm testcase-1.txt
rm testcase-2.txt
gcc wis-untar.c
./a.out > ./program-output/program-output-wis-untar-1.txt
./a.out check.tar > ./program-output/program-output-wis-untar-2.txt
./a.out test.tar > ./program-output/program-output-wis-untar-3.txt
python3 testcasecompare.py