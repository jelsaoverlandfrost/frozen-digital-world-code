def longest_common_prefix(s1, s2):
    if len(s1) < len(s2):
        shorter = s1
    else:
        shorter = s2
    answer_string = ''
    i = 0
    while i < len(shorter):
        if s1[i] == s2[i]:
            answer_string += shorter[i]
            i += 1
        else:
            break
    return answer_string


print "longest_common_prefix ('distance ','disinfection ')"
ans = longest_common_prefix('distance', 'disinfection')
print ans
print "longest_common_prefix ('testing','technical')"
ans = longest_common_prefix('testing', 'technical ')
print ans
print "longest_common_prefix ('drinking ','drinker')"
ans = longest_common_prefix('drinking ', 'drinker')
print ans
print "longest_common_prefix ('rosses','crosses')"
ans = longest_common_prefix('rosses ', 'crosses')
print ans
print "longest_common_prefix ('distancetion','distance')"
ans = longest_common_prefix('distancetion', 'distance')
print ans
