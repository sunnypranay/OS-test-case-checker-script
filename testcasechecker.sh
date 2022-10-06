#!/bin/bash

cp ./original-test-case-file/testcase-1.txt  testcase-1.txt 
cp ./original-test-case-file/testcase-2.txt  testcase-2.txt

gcc ./Assignment/wis-grep.c
./a.out > ./program-output/program-output-wis-grep-1.txt
./a.out hello random.txt> ./program-output/program-output-wis-grep-2.txt
./a.out hello testcase-1.txt> ./program-output/program-output-wis-grep-3.txt
./a.out hello testcase-1.txt testcase-2.txt > ./program-output/program-output-wis-grep-4.txt
gcc ./Assignment/wis-tar.c
./a.out > ./program-output/program-output-wis-tar-1.txt
./a.out test.tar testcase-4.txt testcase-3.txt > ./program-output/program-output-wis-tar-2.txt
./a.out test.tar testcase-1.txt testcase-2.txt > ./program-output/program-output-wis-tar-3.txt
rm testcase-1.txt
rm testcase-2.txt
gcc ./Assignment/wis-untar.c
./a.out > ./program-output/program-output-wis-untar-1.txt
./a.out check.tar > ./program-output/program-output-wis-untar-2.txt
./a.out test.tar > ./program-output/program-output-wis-untar-3.txt

python3 testcasecompare.py