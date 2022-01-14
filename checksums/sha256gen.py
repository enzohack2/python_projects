#!/usr/bin/env python3

import hashlib
import sys

source_checksum = input("[#] Enter source checksum: ")
fpath = input("[#] ABSOLUTE filepath to file from which a checksum will be generated: ")

def checksum_verifier(checksum, filepath):
    """Generates a SHA-256 checksum from file in @filepath and copmares
    it to input @checksum. Informs user if checksum match or otherwise."""

    print("[#] Generating a checksum...")

    with open(filepath, mode="rb") as f:
        data = f.read()

        hash_obj = hashlib.sha256()
        hash_obj.update(data)
        generated_checksum = hash_obj.hexdigest()

        print(f"[#] Generated chechsum: {generated_checksum}")
    
    # Exception handling
    try:
        assert generated_checksum == checksum
        print("[#] Congratulations, the source checksum and application generated checksum match")
        sys.exit(1)

    except AssertionError:
        print("[#] Generated SHA-256 checksum doesn't match with source checksum. Potential issues listed below:")
        print() # spacing
        print("[#] Ceck both inputs are correct: source checksum and filepath leading to executable on your device.")
        print("[#] Redownload your file and try the program again. Good day :)")
        sys.exit(1)

if __name__ == "__main__":
    checksum_verifier(source_checksum, fpath)


# Script works. Thanks for watching :D