import pandas as pd
import hashlib as hl
import re

class HashTypes:
    unsafe = False
    
    def __init__(self, us: bool=False):
        self.unsafe = us
    
    def typeExtractor(self, string, unsafe=True):
        allTypes = hl.algorithms_available if unsafe else hl.algorithms_guaranteed
        print(allTypes)
        pattern = re.compile('^'+string+'\d+[^_]*$' )
        return list(filter(pattern.match, allTypes))
    

    def generateSha(self, noHex=False, types=[]):
        hashList = self.typeExtractor("sha")
        hexdigests = []
        digests = []
        for algo in hashList:
            hash = getattr(hl, algo)
            if noHex==False: 
                hexdigests.append(hash(b"this is a test").hexdigest())
            digests.append(hash(b"this is a test").digest())
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled
    
    def generateSha3(self, noHex=False):
        hashList = self.typeExtractor("sha3_")
        hexdigests = []
        digests = []
        for algo in hashList:
            hash = getattr(hl, algo)
            if noHex==False: 
                hexdigests.append(hash(b"this is a test").hexdigest())
            digests.append(hash(b"this is a test").digest())
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled
        

    def generateBlakes(self, noHex=False, types=[]):
        hashList = self.typeExtractor("blake")
        hexdigests = []
        digests = []
        for algo in hashList:
            hash = getattr(hl, algo)
            if noHex==False: 
                hexdigests.append(hash(b"this is a test").hexdigest())
            digests.append(hash(b"this is a test").digest())
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled
    
    def generateShakes(self, length, noHex=False, types=[]):
        hashList = self.typeExtractor("shake_")
        hexdigests = []
        digests = []
        for algo in hashList:
            hash = getattr(hl, algo)
            if noHex==False: 
                hexdigests.append(hash(b"this is a test").hexdigest(length))
            digests.append(hash(b"this is a test").digest(length))
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled

    def generateOtherHashes(string, noHex=False, types=[]):
        compiled_hashes=[]
        
        return

    def generateCombination(string, algos, types, noHex=False):
        compiled_hashes=[]
        
        return

    def generateAll(string, length, noHex=False):
        compiled_hashes=[]
        
        return
    


def main():
    hashed = HashTypes()
    sha3 = hashed.generateShakes(52)
    print(sha3)
    
if __name__ == "__main__":
    main()