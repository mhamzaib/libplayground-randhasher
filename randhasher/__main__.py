import argparse
from .functions import HashTypes

def main():
    parser = argparse.ArgumentParser(description="Generate a table of hashes for a given string.")
    parser.add_argument("string", help="The string to hash")
    parser.add_argument("-t", "--type", default="sha", help="Hash type: sha, sha3, blake, shake, or all")
    parser.add_argument("-l", "--length", type=int, default=64, help="Length for variable-length hashes (SHAKE)")
    parser.add_argument("--unsafe", action="store_true", help="Include algorithms not guaranteed by the platform")
    parser.add_argument("--no-hex", action="store_true", help="Exclude hex digests from output")

    args = parser.parse_args()
    hasher = HashTypes(unsafe=args.unsafe)

    mapping = {
        "sha": hasher.generateSha,
        "sha3": hasher.generateSha3,
        "blake": hasher.generateBlakes,
        "shake": lambda s, noHex: hasher.generateShakes(s, args.length, noHex),
        "all": lambda s, noHex: hasher.generateAll(s, args.length, noHex)
    }

    result = mapping.get(args.type, hasher.generateSha)(args.string, noHex=args.no_hex)
    
    if result is not None:
        print(result.to_string(index=False))

if __name__ == "__main__":
    main()