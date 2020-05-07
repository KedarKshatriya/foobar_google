def solution(s):
    g_st = s
    s_nu = 1
    st_len = len(g_st)

    for d_val in range(1, st_len):
        sp_lis = []
        if(st_len % d_val == 0):
            for x in range(0, st_len, d_val):
                sp_lis.append(g_st[x:x+d_val])
            sp_lis_leth = len(sp_lis)

            s_nu = sam(sp_lis_leth, sp_lis)
            if(s_nu != 1):
                return s_nu
    return s_nu


def sam(le, sp_lis):
    for i in range(0, le-1):

        if(sp_lis[i] == sp_lis[i+1]):
            if(i == le-2):
                return le
            else:
                continue
        else:
            return 1


r = solution('aabcaabcaabcaabcaabcaabcaabcaabcaabcaabcaabcaabcaabcaabc')
print(r)
