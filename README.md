use.py uses the cmodule
no_use.py is plain python, important for testing
the c module code is compiled by gcc -shared -o libfast_add.so -fPIC fast_add.c
then libfast_add.so is utilized by the python

specifically for dealing with a lot of data, plain python works well with small data and is faster with small data but as the data increases, the operations become a dominant factor which leads to the no_use.py performing better, the larger the data, the more powerful the results
