# A test script will need to return a result code
result_codes = {'TestPass' : 1, 'TestFail' : 2, 'TestAbort' : 3}

# The actual test case would go here. This is just a mock-up or a 'mock'
def my_test_case_mock():
# execute something here
# if it passes you'd return pass, if it failed you'd return fail
    return (result_codes['TestFail'])


# Run my test
result = my_test_case_mock()

# We're all done with the test case
# Print the result code and exit
print(str(result))

exit(0)