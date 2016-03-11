import ctypes as C
mm = C.CDLL('./libmymath.so')

float1=3.5
float2=5.
integer1=2
integer2=5
int_array1=(1,2,3)
int_array2=(4,5,6)
float_array1=(1,2,3)
float_array2=(1,2,3)

#float add_float(float a, float b) {return a + b;}
a = float1
b = float2
mm.add_float.argtypes = [C.c_float, C.c_float]
mm.add_float.restype = C.c_float
print 'add_float funciona: ',a,'+',b,'=',mm.add_float(a,b)


#int add_int(int a, int b) {return a + b;}
a = integer1
b = integer2
mm.add_int.argtypes = [C.c_int, C.c_int]
mm.add_int.restype = C.c_int
print 'add_int funciona: ',a,'+',b,'=',mm.add_int(a,b)


#int add_float_ref(float *a, float *b, float *c) {...; return 0;}
a = C.c_float(float1)
b = C.c_float(float2)
out = C.c_float()
mm.add_float_ref(C.byref(a), C.byref(b), C.byref(out))
print 'add_float_ref funciona: ',a.value,'+',b.value,'=',out.value


#int add_int_ref(int *a, int *b, int *c) {...; return 0;}
a = C.c_int(integer1)
b = C.c_int(integer2)
out = C.c_int()
mm.add_int_ref(C.byref(a), C.byref(b), C.byref(out))
print 'add_int_ref funciona: ',a.value,'+',b.value,'=',out.value


#int add_int_array(int *a, int *b, int *c, int n) {...; return 0;}
n = 3
a = (C.c_int * n) (int_array1[0],int_array1[1],int_array1[2])
b = (C.c_int * n) (int_array2[0],int_array2[1],int_array2[2])
out = (C.c_int * n) (0,0,0)
mm.add_int_array(C.byref(a), C.byref(b), C.byref(out), C.c_int(n))
print 'add_int_array funciona: ',(a[0],a[1],a[2]),'+',(b[0],b[1],b[2]),'=',\
        (out[0],out[1],out[2])


#float dot_product(float *a, float *b, int n) {...; return res;}
n = 3
a = (C.c_float * n) (int_array1[0],int_array1[1],int_array1[2])
b = (C.c_float * n) (int_array2[0],int_array2[1],int_array2[2])
mm.dot_product.restype = C.c_float
print 'dot_product funciona: ',(a[0],a[1],a[2]),'.',(b[0],b[1],b[2]),'=',\
        mm.dot_product(C.byref(a), C.byref(b), C.c_int(n))


