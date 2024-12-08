import random

def keygen(length=64, allowed_characters=None):
    if allowed_characters is None:
        allowed_characters = (
            'qwertyuiopasdfghjklzxcvbnm'
            'QWERTYUIOPASDFGHJKLZXCVBNM'
            '1234567890'
        )
    key = ''.join(random.choice(allowed_characters) for _ in range(length))
    return key

def generate_thighhighs_key():
    segment_length = 6
    thighhighs1_characters = (
        'qwertyuiopasdfghjklzxcvbnm'
        'QWERTYUIOPASDFGHJKLZXCVBNM'
        '1234567890'
    )
    thighhighs2_characters = thighhighs1_characters
    thighhighs3_characters = thighhighs1_characters
    thighhighs4_characters = thighhighs1_characters
    
    key_segments = [
        keygen(segment_length, thighhighs1_characters),
        keygen(segment_length, thighhighs2_characters),
        keygen(segment_length, thighhighs3_characters),
        keygen(segment_length, thighhighs4_characters)
    ]

    key = "Thighhighs-" + "-".join(key_segments)
    return key

key = generate_thighhighs_key()
print(f"Generated Key Successfully: {key}")
