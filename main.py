#OwenG Assignment.

# Read the excel sheet and print the content
# create a loop that does some basic calculation for a million times
# conver the above loop to be done by 8 mutliprocessing jobs. muti threaded
# print out CPU temperature before and after both runs.
# print the time takem by both execution(for loop  & parallelized run)
# print the system properties of your PC
# platform
# CPU specifications
# Number of CPUs
# requirements.txt to hold all the package versions needed to run the script.

import os, platform, psutil, xlrd, pandas as pd, time
import concurrent.futures
def display_system_properties():
    print("="*20, "System Properties", "="*20)
    cpuCount = os.cpu_count()
    uname = platform.uname()
    print(f"System Platform: {uname.system}")
    print(f"Processor: {platform.processor()}")
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
       
    print(f"Number of processors in the system is: {cpuCount}")

def spreadsheetPrinter(filename):
    print("="*20, "SpreadSheet Printout", "="*20)
    dataframe = pd.read_excel(filename)
    print(dataframe)

def basicCalculationMillion():
    print("="*20, "Basic Million Calculation", "="*20)
    result = 0
    for i in range(1000000):
        result += i
    print(result)

def workerCalculation(count):
    print('Worker Calculates')
    result = 0
    for i in range(int(count)):
        result += i
    print(result)


def multiThreadedCalculation():
    maxProcessors = 8
    
    print("="*20, "MultiThreaded Calculation", "="*20)
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=maxProcessors)
    count = 1000000/maxProcessors
    for i in range(maxProcessors):
        pool.submit(workerCalculation(count))

    pool.shutdown(wait=True)





spreadsheetPrinter('inputData.xlsx')
start = time.time()
basicCalculationMillion()
end = time.time()
elapsed_time = end - start
print('Execution Time:', elapsed_time, ' seconds')
start = time.time()
multiThreadedCalculation()
end = time.time()
elapsed_time = end - start
print('Execution Time:', elapsed_time, ' seconds')
display_system_properties()

