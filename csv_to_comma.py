
def main(path):
    with open(path) as f:
        all_lines = f.readlines()

    commad_line = [line.replace(';', ',') for line in all_lines]

    for line in commad_line:
        with open("result.csv", "a") as f:
            f.write(line)


if __name__ == "__main__":
    main(r"C:\Users\ADMIN\Downloads\data\cardio_alco.csv")