
from fractions import Fraction

def solution(m):
    # matrix attributes
    m_size = len(m)
    if m_size >100:
        return -1
    row_sum = [sum(r) for r in m]
    
    if row_sum[0] == 0:
        return [1, 1]
    
    dic_all_row_zero = dict(zip(list(i for i in range(len(m))),list(0 if i == 0 else 1 for i in row_sum)))
    
    dic_all_row_zero = {k: v for k, v in sorted(dic_all_row_zero.items(), key=lambda item: item[1])}
    
    n_rows_all_zeros = list(dic_all_row_zero.values()).count(0)
    
    print("n_rows_all_zeros : ",n_rows_all_zeros)
    
    n_rows_all_non_zeros = len(m) - n_rows_all_zeros
    
    print("n_rows_all_non_zeros",n_rows_all_non_zeros)
    arr = np.array(m)
    
#     print(arr)
    print(dic_all_row_zero.keys())
    arr_r = arr[list(dic_all_row_zero.keys()), :]
    print(arr_r)
    arr_c = arr_r[:, list(dic_all_row_zero.keys())]
#     print(arr_c)
    new_r_sum = [sum(r) for r in arr_c]
    
    new_m = []
    for i in range(len(arr_c)):
        new_m.append(list(map(lambda x: 0 if new_r_sum[i] == 0 
                            else x / new_r_sum[i], arr_c[i])))

    newarr = np.array(new_m)
    print(newarr)
    
    Q = newarr[n_rows_all_zeros:, n_rows_all_zeros:]
    R = newarr[n_rows_all_zeros:, :n_rows_all_zeros]
    ImQ = np.subtract(np.identity(n_rows_all_non_zeros), Q)
    F = np.linalg.inv(ImQ)
    FR = np.matmul(F, R)
    FRf = []
    for i in range(n_rows_all_non_zeros):
        FRf.append([Fraction.from_float(x).limit_denominator(max_denominator = 2**32) for x in FR[i]])

    print(FRf)
    maxd = max(list(map(lambda x: x.denominator, FRf[0])))
    indv = list(map(lambda x: (x*maxd).numerator, FRf[0]))
    return list(indv + [maxd])