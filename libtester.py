import ctypes as C
mm = C.CDLL('./libmymath.so')

#float add_float(float a, float b) {return a + b;}
a=2
b=5
mm.add_float.argtypes = [C.c_float,C.c_float]
mm.add_float.restype = C.c_float
print(mm.add_float(a,b))


#int add_int(int a, int b) {return a + b;}
a=2
b=5
mm.add_int.argtypes = [C.c_int,C.c_int]
mm.add_int.restype = C.c_int
print(mm.add_int(a,b))

#int add_float_ref(float *a, float *b, float *c) {*c = *a + *b; return 0;}
a=C.c_float(2)
b=C.c_float(5)
out=C.c_float()
mm.add_float_ref(C.byref(a),C.byref(b),C.byref(out))
print(out.value)


#int add_int_ref(int *a, int *b, int *c) {*c = *a + *b; return 0;}
a=C.c_int(2)
b=C.c_int(5)
out=C.c_int()
mm.add_int_ref(C.byref(a),C.byref(b),C.byref(out))
print(out.value)

#int add_int_array(int *a, int *b, int *c, int n) {
#  int i;
#  for (i = 0; i < n; i++) {
#    c[i] = a[i] + b[i];
#  }
#  return 0;
#}
a=(C.c_int * 3) (1,2,3)
b=(C.c_int * 3) (4,5,6)
out=(C.c_int * 3) (0,0,0)
n=3#n=C.c_int(3)
mm.add_int_array(C.byref(a),C.byref(b),C.byref(out),C.c_int(n))
print(out[0],out[1],out[2])
print(out)

#float dot_product(float *a, float *b, int n) {
#  float res;
#  int i;
#  res = 0;
#  for (i = 0; i < n; i++) {
#    res = res + a[i] * b[i];
#  }
#  return res;
#}
