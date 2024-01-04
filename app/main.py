def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = ""
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines += line + "\n"

    with open(file_name, "w") as file:
        file.write(lines)


if __name__ == "__main__":
    main()
