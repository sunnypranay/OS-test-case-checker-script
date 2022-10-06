# This program is used to compare the output of two test cases
# and print test case pass if the output is same and test case fail
# if the output is different.
print("--------------------WIS-GREP TEST CASE RESULTS---------------------")
test_case_count = 0
for i in range(1, 5):
    filename = "./original-output/original-output-wis-grep-" + str(i) + ".txt"
    original_output = open(filename, "r")
    filename = "./program-output/program-output-wis-grep-" + str(i) + ".txt"
    program_output = open(filename, "r")

    # compare original output and program output
    if original_output.read() == program_output.read():
        print("Test case wis-grep -", i,"pass")
        test_case_count += 1
    else:
        print("Test case wis-grep -", i,"fail")

    original_output.close()
    program_output.close()
print("Total test cases passed:", test_case_count)
print()
print("--------------------WIS-TAR TEST CASE RESULTS---------------------")
test_case_count = 0
for i in range(1,3):
    filename = "./original-output/original-output-wis-tar-" + str(i) + ".txt"
    original_output = open(filename, "r")
    filename = "./program-output/program-output-wis-tar-" + str(i) + ".txt"
    program_output = open(filename, "r")

    # compare original output and program output
    if original_output.read() == program_output.read():
        print("Test case wis-tar -", i,"pass")
        test_case_count += 1
    else:
        print("Test case wis-tar -", i,"fail")
    
    original_output.close()
    program_output.close()

program_output_1 = open("testcase-1.txt", "r")
program_output_2 = open("testcase-2.txt", "r")
original_output_1 = open("./original-test-case-file/testcase-1.txt", "r")
orginal_output_2 = open("./original-test-case-file/testcase-2.txt", "r")

print_status = False
# compare original output and program output
if original_output_1.read() == program_output_1.read() and orginal_output_2.read() == program_output_2.read():
    print("Test case wis-tar - 3 pass")
    test_case_count += 1
    print_status = True
else:
    print("Test case wis-tar - 3 fail")
    print_status = False

program_output_1.close()
program_output_2.close()
original_output_1.close()
orginal_output_2.close()
print("Total test cases passed:", test_case_count)

print()
print("--------------------WIS-UNTAR TEST CASE RESULTS---------------------")

test_case_count = 0
for i in range(1,3):
    filename = "./original-output/original-output-wis-untar-" + str(i) + ".txt"
    original_output = open(filename, "r")
    filename = "./program-output/program-output-wis-untar-" + str(i) + ".txt"
    program_output = open(filename, "r")

    # compare original output and program output
    if original_output.read() == program_output.read():
        print("Test case wis-untar -", i,"pass")
        test_case_count += 1
    else:
        print("Test case wis-untar -", i,"fail")
    
    original_output.close()
    program_output.close()

if print_status:
    print("Test case wis-untar - 3 pass")
    test_case_count += 1
else:
    print("Test case wis-untar - 3 fail")

print("Total test cases passed:", test_case_count)