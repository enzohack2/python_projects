#!/usr/bin/env python3

import hashlib
import sys

source_checksum = input("[#] Enter download source checksum: ")
fpath = input("[#] Enter ABSOLUTE filepath for file to generate checksum: ")

def checksum_verifier(checksum, filepath):
    """Generates a SHA-256 checksum from file in @filepath and compares it to input @checksum and informs the user if checksums match or otherwise."""

    print("[#] Generating a checksum...")

    with open(filepath, mode="rb") as f:
        data = f.read()

        hash_obj = hashlib.sha256()
        hash_obj.update(data)
        generated_checksum = hash_obj.hexdigest()

        print(f"[#] Generated checksum: {generated_checksum}")

    try:
        assert generated_checksum == checksum
        print("[#] Yay! Generated checksum matches download source SHA-256 checksum. Good day :)")
        sys.exit(1)
    except AssertionError:
        print("[#] Generated SHA-256 checkusm doesn't match with source checksum. Potential issues listed below...")
        print()
        print("[#] Check your inputs are correct, both the download source SHA-256 checksum and the correct filepath")
        print("[#] The file is possibly corrupt, did you download it from it's original source or an unregistered download mirror?")
        print("[#] Redownload your file and try the program again")
        print("[#] Good day :)")
        sys.exit(1)

if __name__ == "__main__":
    checksum_verifier(source_checksum, fpath)