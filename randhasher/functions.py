import pandas as pd
import hashlib as hl
import re

class HashTypes:
    def __init__(self, unsafe: bool = False):
        self.unsafe = unsafe
    
    def typeExtractor(self, string, unsafe=None):
        target_unsafe = unsafe if unsafe is not None else self.unsafe
        allTypes = hl.algorithms_available if target_unsafe else hl.algorithms_guaranteed
        pattern = re.compile('^' + string + r'\d*[^_]*$')
        return list(filter(pattern.match, allTypes))
    
    def generator(self, hashtype: str, string: str, length=0, noHex=False):
        try: 
            hashList = self.typeExtractor(hashtype)
            if not hashList:
                available = hl.algorithms_available if self.unsafe else hl.algorithms_guaranteed
                raise ValueError(f"No hashes found for '{hashtype}'.")
        except Exception as e:
            print(f"Error: {e}")
            return None

        return self._manual_batch_generator(hashList, string, length=length, noHex=noHex)

    def generateSha(self, string, noHex=False):
        return self.generator('sha', string, noHex=noHex)
    
    def generateSha3(self, string, noHex=False):
        return self.generator('sha3_', string, noHex=noHex)
        
    def generateBlakes(self, string, noHex=False):
        return self.generator('blake', string, noHex=noHex)
    
    def generateShakes(self, string, length, noHex=False):
        return self.generator('shake', string, length=length, noHex=noHex)

    def generateOtherHashes(self, string, noHex=False):
        major_families = ['sha', 'blake', 'shake']
        all_algos = hl.algorithms_available if self.unsafe else hl.algorithms_guaranteed
        others = [a for a in all_algos if not any(fam in a.lower() for fam in major_families)]
        return self._manual_batch_generator(others, string, noHex=noHex)

    def generateCombination(self, string, algos, noHex=False):
        if not isinstance(algos, list):
            raise ValueError("The 'algos' parameter must be a list of strings.")
        return self._manual_batch_generator(algos, string, noHex=noHex)

    def generateAll(self, string, length=64, noHex=False):
        all_algos = list(hl.algorithms_available if self.unsafe else hl.algorithms_guaranteed)
        return self._manual_batch_generator(all_algos, string, length=length, noHex=noHex)

    def _manual_batch_generator(self, algo_list, string, length=0, noHex=False):
        hexdigests = []
        digests = []
        valid_algos = []
        estring = string.encode('utf-8')
        
        for algo in algo_list:
            try:
                h = hl.new(algo, estring)
                kwargs = {'length': length} if "shake" in algo.lower() else {}
                
                if not noHex:
                    hexdigests.append(h.hexdigest(**kwargs))
                
                digests.append(h.digest(**kwargs))
                valid_algos.append(algo)
            except Exception:
                continue
      
        compiled = pd.DataFrame({
            'Algo': valid_algos, 
            'Digest': digests
        })
        
        if not noHex:
            compiled['HexDigests'] = hexdigests
            
        return compiled
