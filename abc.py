import hashlib
import time
import secrets
import string
import sys

max_nonce = 2 ** 32  # 4 billion


def proof_of_work(header, target):
    for nonce in range(max_nonce):
        data = header.encode() + nonce.to_bytes(4, byteorder='big')
        hash_value = hashlib.sha256(hashlib.sha256(data).digest()).digest()
        if int.from_bytes(hash_value, byteorder='big') < target:
            return nonce
    return None


if __name__ == '__main__':

    # Calculate hash rate
    start_time = time.time()
    num_hashes = 0
    while True:
        data = ''.join(secrets.choice(string.ascii_letters) for i in range(50)).encode() + \
               secrets.randbits(32).to_bytes(4, byteorder='big')
        hash_value = hashlib.sha256(hashlib.sha256(data).digest()).digest()
        num_hashes += 1
        if time.time() - start_time >= 1:
            hash_rate = num_hashes / (time.time() - start_time)
            print(f'Hash rate: {hash_rate:.2f} hashes per second')
            break

    # Find nonce for different difficulty levels
    # for difficulty in range(5, 31):
    difficulty = int(sys.argv[1]) 
    target = 2 ** (256 - difficulty)
    print(f'Difficulty target: {target}')

    block_header = ''.join(secrets.choice(string.ascii_letters) for i in range(50))
    print(f'Header: {block_header}')

    start_time = time.time()
    nonce = proof_of_work(block_header, target)
    end_time = time.time()

    if nonce != None:
        print(f'Nonce: {nonce}')
        print(f'Time: {end_time - start_time:.6f} seconds')
    else:
        print('Failed')
