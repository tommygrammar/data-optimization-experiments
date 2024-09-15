use.py uses the cmodule
no_use.py is plain python, important for testing
the c module code is compiled by gcc -shared -o libfast_add.so -fPIC fast_add.c
then libfast_add.so is utilized by the python
