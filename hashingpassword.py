import hashlib
print(hashlib.algorithms_available)
def calculate_md5(data):
# Convert data to bytes if it’s not already

# Calculate SHA-256 hash
    sha256_hash = hashlib.md5(data).hexdigest()

    return sha256_hash

# Example usage:
input_data = str(input("het mot de passe : ")).encode()
hash_value = calculate_md5(input_data)
print(input_data,"is : ", hash_value)

