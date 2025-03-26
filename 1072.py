def maxEqualRowsAfterFlips(matrix: list[list[int]]) -> int:

    m, n = len(matrix), len(matrix[0])
    
    # rownum maps to list of cols to flip
    row_hashes: dict[int, list[int]] = {}
    for rownum, row in enumerate(matrix):
        # First we find out the majority
        row_hash = {1: [], 0: []}
        for colnum, col in enumerate(row):
            row_hash[col].append(colnum)

        if n in (len(row_hash[0]), len(row_hash[1])):
            row_hashes[rownum] = []
        elif len(row_hash[0]) > len(row_hash[1]):
            row_hashes[rownum] = row_hash[0]
        else:
            row_hashes[rownum] = row_hash[1]

    res_to_flip = set(row_hashes[0])
    max_cols = 0
    for row_hash in row_hashes.values():
        max_cols = max(max_cols, len(row_hash))
        res_to_flip.intersection_update(set(row_hash))
    
    # Now that we know which columns to flip (maybe)

    return len(res_to_flip) or max_cols

print(maxEqualRowsAfterFlips([[0,1],[1,1]]))
print(maxEqualRowsAfterFlips([[0,1],[1,0]]))
print(maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))