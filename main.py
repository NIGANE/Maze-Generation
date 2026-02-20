from dotenv import dotenv_values


def main() -> None:
    env = {**dotenv_values()}
    try:
        conf_file: str | None = env.get('conf_file')
        content: str = open(conf_file or "config.txt", 'r').read()
    except FileNotFoundError:
        print(f"Error: configuration file '{conf_file}'")
        return
    print(content)


main()