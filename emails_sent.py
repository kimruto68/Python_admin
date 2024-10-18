def main():
    names = ["Mario", "Erick", "Ednah", "Devis"]
    for name in names:
        print(write_letter(name, "Surf Channel"))


def write_letter(receiver, sender):
    return (
        "***************************************************\n"
        f"    Dear {receiver},\n\n"
        "    You are invited for the Club Session TODAY\n"
        "    at 4:30PM. Come prepared for a dance and\n"
        "    some fun games!!\n\n"
        f"    Sincerely,\n"
        f"    {sender}\n"
        "***************************************************"
    )

main()

