for privatekey in keys_list:
    # Decrypt the ciphertext using the private key.
    plaintext = privatekey.decrypt(ciphertext)  
