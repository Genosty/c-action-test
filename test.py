import os, subprocess

# Settings
TEST_DIR = "."     # Directory with our program
CODE_FILE = "main.c"    # our c code 
COMPILER_TIMEOUT = 10.0 #COMPILER TIMEOUT (SECONDS)
RUN_TIMEOUT = 10.0

# Create absolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

#Compile the program
print("building...")
try:
        ret = subprocess.run(["gcc", code_path, "-o", app_path],
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE,
                                timeout = COMPILER_TIMEOUT)

except Exception as e:
        print("ERROR: Compilation failed.", str(e))
        exit(1)

#Parse output. this step just to capptcher the error code in a string in python then print it to the console
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)
#محمد الغيثي

# Check to see if the program comiled successfully
if ret.returncode != 0:
        print("Compilation failed.")
        exit(1)


print("Running...")
try:
        ret = subprocess.run([app_path],
                                stdout = subprocess.PIPE,
                                timeout = COMPILER_TIMEOUT)

except Exception as e:
        print("ERROR: Compilation failed.", str(e))
        exit(1)

#pars output 
output = ret.stdout.decode('utf-8')
print(output)
#محمد الغيثي

#all test passed successfully , Exit gracefully
print("All tests passed!")
exit(0)