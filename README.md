# test_gropro
Test run for GoPro of 2024


## Usage
Make sure you are in the top-level-directory of the whole project.
Your ``ls -l`` output should look something like this:

```
❱ ls -l
total 7784
-rw-r--r--   1 odruska  staff      486 May  3 09:14 README.md
-rwxr-xr-x   1 odruska  staff       81 May  3 09:14 TEST_GROPRO_2024.sh
drwx------@ 32 odruska  staff     1024 May  3 07:26 docu
drwxr-xr-x@  5 odruska  staff      160 May  2 14:42 input
-rw-r--r--@  1 odruska  staff  3971378 May  1 21:01 matse_test_gropro_2024_aufgabenstellung.pdf
drwxr-xr-x@  5 odruska  staff      160 May  3 08:33 output
drwxr-xr-x@ 14 odruska  staff      448 May  3 09:11 source
```

Make sure to have gnuplot and python3.x installed.
``which gnuplot`` and ``which python3`` should both yield output.

To start running the examples and all my test cases, simply do:
``./TEST_GROPRO_2024.sh``

This project makes use of a Python Virtual Environment.
It is located under ``./venv_test_gropro_2024`` and should be activated
by the given ShellScript without further action.

gnuplot should already haven opened one window per test case, showing the gnuplot
graphic for each test case.

It could be that all gnuplot windows overlay each other exactly.
Dont be fooled by that ;-) (I was...)
