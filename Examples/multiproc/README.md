# Comparing Python 3.9.2 on PiOS Bullseye
# Threading vs. Multi-Processing for CPU and I/O bound operations

Examples run on Raspberry Pi 4B  1.5GHz 4-core Cortex-A72 (ARM v8)
with Python3.9.2

For this test - multiprocessing and threading had similar results for i/o bound,  
but multi-processing was more efficient than threading for cpu-bound.  

# Using threads (Examples/threads):
Typical Result:  
$ ./compare_io.py  
.  Starting 4000 cycles of io-bound threading  
.  Sequential run time: 45.30 seconds  
.  4 threads Parallel run time: 13.06 seconds  
.  2 threads Parallel - twice run time: 24.14 seconds  

Typical Result:  
$ ./compare_cpu.py  
.  Starting 4000000 cycles of cpu-only threading  
.  Sequential run time: 2.59 seconds  
.  4 threads Parallel run time: 3.62 seconds  
.  2 threads Parallel twice - run time: 2.96 seconds  

Typical Result:  
$ ./compare_cpu_wSleep.py  
.  Starting 4000000 cycles of cpu-only threading with a yield  
.  Sequential run time: 11.18 seconds  
.  4 threads Parallel run time: 41.74 seconds  
.  2 threads Parallel twice - run time: 24.05 seconds  






# Using multiprocessing (Examples/multiproc):  
Typical Result:  
$ ./compare_io.py   
.  Starting 4000 cycles of io-bound processing  
.  Sequential - run time: 45.22 seconds  
.  4 procs Parallel - run time: 12.82 seconds  
.  2 procs Parallel twice - run time: 23.93 seconds  

Typical Result:  
$ ./compare_cpu.py  
.  Starting 4000000 cycles of cpu-only processing  
.  Sequential run time: 2.62 seconds  
.  4 procs Parallel - run time: 0.70 seconds  
.  2 procs Parallel twice - run time: 1.33 seconds  

