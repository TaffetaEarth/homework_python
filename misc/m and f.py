# def F(n):
#     if n == 0:
#         return 1
#     else:
#         return n - M(F(n - 1))
#
#
# def M(n):
#     if n == 1:
#         return 0
#     else:
#         return n - F(M(n - 1))


f = lambda n: 0 if n == 0 else n - m(f(n - 1))
m = lambda n: 1 if n == 0 else n - f(m(n - 1))
print(m(100))
