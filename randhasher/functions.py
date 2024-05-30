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
    
    def generator(self, hashtype: str, string: str, length=0, noHex=False):
        hashList = self.typeExtractor(hashtype)
        hexdigests = []
        digests = []
        estring = string.encode('utf-8')
        for algo in hashList:
            hash = getattr(hl, algo)
            kwargs = {'length': length} if hashtype.startswith("shake") else {}
            if noHex==False: 
                hexdigests.append(hash(estring).hexdigest(**kwargs))
            digests.append(hash(estring).digest(**kwargs))
        compiled = pd.DataFrame({'Algo': hashList, 'Digest': digests})
        if noHex==False:
            compiled['HexDigests'] = hexdigests
        return compiled
    

    def generateSha(self, string, noHex=False):
        return self.generator('sha', string, noHex=noHex)
    
    def generateSha3(self, string, noHex=False):
        return self.generator('sha3_', string, noHex=noHex)
        

    def generateBlakes(self, string, noHex=False):
        return self.generator('blake', string, noHex=noHex)
    
    def generateShakes(self, string, length, noHex=False):
        return self.generator('shake_', string, length=length, noHex=noHex)

    def generateOtherHashes(string, noHex=False):
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
    sha3 = hashed.generateBlakes("This works")
    print(sha3)
    
if __name__ == "__main__":
    main()