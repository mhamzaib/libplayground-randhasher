import pandas as pd
import hashlib as hl
import re

class HashTypes:
    unsafe = False
    
    def __init__(self, us: bool=False):
        self.unsafe = us
    
    def typeExtractor(self, string, unsafe=False):
        allTypes = hl.algorithms_available if unsafe else hl.algorithms_guaranteed
        pattern = re.compile(string + "*.")
        return list(filter(pattern.match, allTypes))
    

    def generateSha(self, noHex=False, types=[]):
        hashList = self.typeExtractor("sha")
        return self.generator(hashList, noHex)        
        return
    
    def generateSha3(self, noHex=False):
        hashList = self.typeExtractor("sha3_")
        return self.generator(hashList, noHex)
        

    def generateBlakes(string, noHex=False, types=[]):
        compiled_hashes=[]
        
        return

    def generateOtherHashes(string, noHex=False, types=[]):
        compiled_hashes=[]
        
        return

    def generateCombination(string, types, noHex=False):
        compiled_hashes=[]
        
        return

    def generateAll(string, noHex=False):
        compiled_hashes=[]
        
        return
    
    def generator(self, hashList, noHex=False):
        print(hashList)
        hexdigests = []
        digests = []
        for algo in hashList:
            print(algo)
            hash = getattr(hl, algo)
            if noHex==False: 
                hexdigests.append(hash(b"this is a test").hexdigest())
            digests.append(hash(b"this is a test").digest())
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled

def main():
    hashed = HashTypes()
    sha3 = hashed.generateSha()
    print(sha3)
    
if __name__ == "__main__":
    main()