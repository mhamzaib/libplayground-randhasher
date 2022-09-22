import hashlib as hl
import re

class HashTypes:
    unsafe = False
    
    def __init__(self, us: bool):
        self.unsafe = us
    
    ## TODO: Recieve failure : pattern is not callable -> fix
    def typeExtractor(string, unsafe=False):
        allTypes = hl.algorithms_available if unsafe else hl.algorithms_guaranteed
        pattern = re.compile(string+"*.")
        return list(filter(pattern, allTypes))
    
    sha = typeExtractor('sha')
    blake = typeExtractor('blake')
    

    def generateSha(string, noHex=False, types=[]):
        compiled_hashes=[]
        
        return
    
    def generateSha3(string, noHex=False, types=[]):
        compiled_hashes=[]
        
        return    

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