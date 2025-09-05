def parse_log(file_path):
    with open(file_path,"r") as file:
        for line in file:
            if "ERROR" in line:
                print(line)


if __name__ == "__main__":
    log_file="app.log"
    parse_log(log_file)     