# Encoder & Decoder:
def encode_or_decode(text):
    encode = text[::-1]

    output = f"Mode: encode. Encoded: {encode}. Mode: decoded. Decoded: {text}."

    return output

text = input("Enter text: ")

print(encode_or_decode(text))