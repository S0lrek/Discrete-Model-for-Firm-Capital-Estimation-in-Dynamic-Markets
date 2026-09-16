def transpose(B) -> list:
    Z = []
    for i in range(len(B[0])):
        A = []
        for row in B:
            A.append(row[i])
        Z.append(A)
    return Z

def matrix_multiplier(A, B) -> list:
    Z = []
    X = transpose(B)
    for row in A:
        Y = []
        for column in X:
            a = 0
            for l in range(len(row)):
                a += (row[l] * column[l])
            Y.append(a)
        Z.append(Y)
    return Z

def check_square_matrix(A) -> bool:
    for row in A:
        if len(A) == len(row):
            return True
        else:
            return False

def identity_matrix(n) -> list:
    B = []
    for i in range(n):
        A = []
        for m in range (n):
            if m != i:
                A.append(0)
            else:
                A.append(1)
        B.append(A)
    return B

def matrix_power(A, n) -> list:
    if check_square_matrix(A) != True:
        return False
    elif n == 0:
        return identity_matrix(len(A))
    elif n == 1:
        return A
    elif n >= 2:
        Z = matrix_multiplier(A, A)
        for i in range(n - 2):
            Z = matrix_multiplier(Z, A)
        return Z
    
def matrix_liner(A) -> list:
    Z = []
    for row in A:
        for i in range(len(row)):
            Z.append(row[i])
    return Z

def matrix_deliner(B, m) -> list:
    Z = []
    for i in range(m):
        Y = []
        for n in range(m):
            Y.append(B[n + m*i])
        Z.append(Y)
    return Z          

def matrix_addition(A, B) -> list:
    C = matrix_liner(A)
    D = matrix_liner(B)
    E = []
    for i in range(len(C)):
        f = C[i] + D[i]
        E.append(f)
    G = matrix_deliner(E, len(A[0]))
    return G

def vector_addition(v, u):
    A = []
    B = matrix_liner(v)
    C = matrix_liner(u)
    for i in range(len(B)):
        E = []
        d = B[i] + C[i]
        E.append(d)
        A.append(E)
    return A

def zero_matrix(n, m) -> list:
    B = []
    for i in range(n):
        A = []
        for l in range (m):
            A.append(0)
        B.append(A)
    return B

def geometric_sum0(A, n) -> list:
    Z = zero_matrix(len(A), len(A))
    for i in range(n + 1):
        Y = matrix_power(A, i)
        Z = matrix_addition(Z, Y)
    return Z

def geometric_sum(A, n) -> list:
    Z = zero_matrix(len(A), len(A))
    Y = identity_matrix(len(A))
    I = identity_matrix(len(A))
    if n < 0:
        return Z
    else:   
        for i in range(n):
            Y = matrix_multiplier(Y, A)
            Z = matrix_addition(Z, Y)
    Z = matrix_addition(Z, I)
    return Z

def scalar_multiplier(A, l):
    B = []
    for row in A:
        C = []
        for i in range(len(row)):
            C.append(l * row[i])
        B.append(C)
    return B

def capital_flow(S, n, Q, D):
    sn = matrix_power(S, n)
    snq = matrix_multiplier(sn, Q)
    sum_s = geometric_sum(S, n - 1)
    d = matrix_multiplier(sum_s, D)
    d = scalar_multiplier(d, -1)
    E = vector_addition(snq, d)
    return E