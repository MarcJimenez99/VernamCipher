def random_generator(cipher_list, root):
    i = 0
    A = 7
    B = 0
    N = 257
    random_list = []
    random_list.append(root)
    while (i < len(cipher_list)):
        temp = ((random_list[i] * A) + B) % N
        random_list.append(temp)
        i += 1
    return random_list         

def solve(cipher_list, random_list):
    N = 257
    i = 0
    secret_message = []
    while i < len(cipher_list):
        #print(f'Values: {cipher_list[i]} - {random_list[i]} \n')
        temp = (int(cipher_list[i]) - random_list[i])
        if (temp < 0):
            temp2 = 256 - abs(temp) 
            temp = temp2
        else:
            temp = temp % N
        secret_message.append(temp)
        i += 1
    return secret_message

def decrypt(secret_message):
    Decrypted_text = ""
    i = 0
    for element in secret_message:
        Decrypted_text = Decrypted_text + chr(secret_message[i])
        i += 1
    return Decrypted_text


ciphertext = "140 91 200 218 25 59 219 201 172 20 42 223 32 13 135 110 12 113 184 191 36 115 41 187 127 216 141 61 168 230 40 163 195 46 17 13 51 45 208 137 113 103 162 75 237 48 77 160 44 104 79 179 88 108 149 130 120 151 1 147 99 94 238 129 215 175 166 103 160 174 155 16 6 1 215 122 41 170 240 128 101 113 246 133 233 146 17 234 63 164 120 207 248 41 89 249 45 200 7 188 153 65 58 8 87 42 81 197 164 4 223 127 237 67 210 22 99 242 106 15 198 10 0 6 88 146 186 37 32 124 29 210 18 140 246 232 222 112 162 254 125 226 62 37 117 86 35 32 112 77 158 24 13 203 86 86 181 190 115 244 216 70 141 152 48 131 197 30 222 49 243 91 130 229 75 55 171 104 81 209 116 52 240 255 14 14 173 152 233 86 244 14 195 244 236 62 246 240 250 159 149 162 210 45 63 151 94 10 66 53 98 18 165 223 151 221 76 202 58 9 220 101 83 157 124 20 215 28 80 143 7 127 57 87"

cipher_list = []
cipher_list = ciphertext.split()

#print (cipher_list)

root = (int(cipher_list[0]) - 70) % 256

random_list = random_generator(cipher_list, root)

secret_message = solve(cipher_list, random_list)

Decrypted_text = decrypt(secret_message)

print(Decrypted_text)

