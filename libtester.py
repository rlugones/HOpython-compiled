import ctypes as C
mm = C.CDLL('./libmymath.so')


float add_float(float a, float b) {return a + b;}
int add_int(int a, int b) {return a + b;}
int add_float_ref(float *a, float *b, float *c) {*c = *a + *b; return 0;}
int add_int_ref(int *a, int *b, int *c) {*c = *a + *b; return 0;}
int add_int_array(int *a, int *b, int *c, int n) {
  int i;
  for (i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
  }
  return 0;
}

float dot_product(float *a, float *b, int n) {
  float res;
  int i;
  res = 0;
  for (i = 0; i < n; i++) {
    res = res + a[i] * b[i];
  }
  return res;
}
