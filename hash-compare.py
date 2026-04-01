import hashlib

message = input("Enter message: ")

h = hashlib.sha256(message.encode())
hex_dgst = h.hexdigest()

print("Original message: ", message)
print("SHA-256 digest: ", hex_dgst)

message2 = input("Enter second message: ")

h2 = hashlib.sha256(message2.encode())
hex_dgst2 = h2.hexdigest()

print("Hash of second message: ", hex_dgst2)

if hex_dgst == hex_dgst2:
    print("The hashes match")
else:
    print("The hashes do not match")
