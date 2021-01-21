# Auto compiler for Cython

This WiP project automatically tries to make programs faster, by running a program with a list of data,
and finding vars that dont change type, and then creating a cdef for them, so cython will optimise them.