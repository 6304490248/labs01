emp_recs = [(1, 'Nick', 23, 45000.0),
            (2, 'nick jr.', 34, 24000.0),
            (3, 'nick sr.',53, 145000.0),
            (4, 'dan', 23, 45000.0),
            (5, 'steve',23, 46000.0)]
print(sorted(emp_recs, key=lambda x:x[3], reverse = True))
print(max(emp_recs, key=lambda x:x[0]))