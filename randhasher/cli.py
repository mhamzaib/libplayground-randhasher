import argparse
import sys
from randhasher.functions import HashTypes
from rich.console import Console
from rich.table import Table


def main():
    parser = argparse.ArgumentParser(
        description="randhasher: Generate structured hash comparison tables."
    )
    parser.add_argument("string", help="The string you want to hash")
    parser.add_argument(
        "-t", "--type", 
        default="sha", 
        choices=["sha", "sha3", "blake", "shake", "all", "other"],
        help="The family of hashes to generate (default: sha)"
    )
    parser.add_argument(
        "-l", "--length", 
        type=int, 
        default=64, 
        help="Length for variable-length hashes like SHAKE (default: 64)"
    )
    parser.add_argument(
        "--no-hex", 
        action="store_true", 
        help="Exclude the HexDigest column from the output"
    )
    parser.add_argument(
        "--unsafe", 
        action="store_true", 
        help="Include algorithms not guaranteed by your platform"
    )

    args = parser.parse_args()
    hasher = HashTypes(unsafe=args.unsafe)

    try:
        if args.type == "sha":
            df = hasher.generateSha(args.string, noHex=args.no_hex)
        elif args.type == "sha3":
            df = hasher.generateSha3(args.string, noHex=args.no_hex)
        elif args.type == "blake":
            df = hasher.generateBlakes(args.string, noHex=args.no_hex)
        elif args.type == "shake":
            df = hasher.generateShakes(args.string, args.length, noHex=args.no_hex)
        elif args.type == "other":
            df = hasher.generateOtherHashes(args.string, noHex=args.no_hex)
        else:
            df = hasher.generateAll(args.string, args.length, noHex=args.no_hex)

        if df is not None:
            console = Console()
            table = Table(title="Hash Comparison Results", show_lines=True)

            table.add_column("Algo", style="cyan", no_wrap=True)
            table.add_column("Digest", style="magenta", overflow="fold")
            table.add_column("HexDigests", style="green", overflow="fold")

            for _, row in df.iterrows():
                table.add_row(
                    str(row['Algo']), 
                    str(row['Digest']), 
                    str(row['HexDigests'])
                )

            console.print(table)

            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()