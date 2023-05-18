

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    text = input("[*] Type Your Feeling : ")
    converted_text = convert(text)
    print(converted_text)


main()
# === OutPut ===

# [*] Type Your Feeling : Im Happy :)
# Im Happy 🙂
