# VernamCipher

We've been given an alternate version of the vernam cipher that encrypts text through the formula C_i = (P_i + R_i) mod N, Where R_i
comes from our given random number generater LCG, R_i+1 = (R_i * A) + B (mod N). This code decrypts our given ciphertext and outputs
the secret message.
