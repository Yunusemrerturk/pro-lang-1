from gcd_exp import *

def toChunks(m, chunkSize):
    chunk_m = []
    for ch in m:
        chunk_m.append(ord(ch).__str__())
    chunk_m_str = string.join(chunk_m, sep='')
    chunks = []
    sz = len(chunk_m_str)
    adet = (sz/chunkSize)
    for i in range(1,adet+1):
        iba = (i - 1) * chunkSize
        iso = iba + chunkSize
        chunks.append(chunk_m_str[iba:iso])
    if not (adet*chunkSize) == sz:
        iba = iso
        iso = sz
        chunks.append(chunk_m_str[iba:iso])
    return chunks
    
def chunksToPlain(m):
    #todo
    return True


