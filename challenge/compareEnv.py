# given list of attributes of a,b in the form
# "attribute=value"
# return sorted list of string indicates
# - attribute is only in a or b
# - attribute in a and b but has different value

def compareEnv(a, b):
    s1 = " is only in "
    s2 = " is different"
    
    ref_a = {x:y for u in a for x,y in [u.split("=")]}
    ref_b = {x:y for u in b for x,y in [u.split("=")]}
    
    same_keys = {*ref_a}&{*ref_b}
    diff_keys = {*ref_a}^{*ref_b}
    
    result = [x+s2 for x in same_keys if ref_a[x]!=ref_b[x]] + [x+s1+"A" if x in ref_a else x+s1+"B" for x in diff_keys]
    
    return sorted(result)
