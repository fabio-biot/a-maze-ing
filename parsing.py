def parse():
    parsed = {}
    with open("config.txt", "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            parsed[key] = value
    return parsed



def main():
    parsed = parse()
    for key, value in parsed.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
