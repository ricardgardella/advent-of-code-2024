def __get_rules(data: str) -> dict:
    rules = {}
    for line in data.strip().split('\n'):
        line = line.strip().split('|')
        if int(line[0]) not in rules:
            rules[int(line[0])] = []
        rules[int(line[0])].append(int(line[1]))
    return rules

def __check_message(message: list, rules: dict) -> bool:
    
    for i in range(len(message)):
        value = message[i]
        rules_value = rules.get(value, [])
        if len(rules_value) == 0:
            continue
        for j in range(0, len(message[0:i])):
            if message[j] in rules_value:
                return False
    return True

def __fix_incorrect_message(message: list, rules: dict) -> list:
    for i in range(len(message)):
        value = message[i]
        rules_value = rules.get(value, [])
        if len(rules_value) == 0:
            continue
        for j in range(len(message[0:i]) - 1, -1, -1):
            value_j = message[j]
            if value_j in rules_value:
                message = list(message)
                message[i] = message[j]
                message[j] = value
                message = tuple(message)
                return message
    return message


def part_1(data: str) -> int:
    rules, messages = data.strip().split("\n\n")
    rules = __get_rules(rules)
    middle_count = 0
    for message in messages.strip().split("\n"):
        message = eval(message)
        if __check_message(message, rules):
            middle_count += int(
                message[len(message) // 2]
            )  # Adds the middle character of the message string converted to integer
    return middle_count


def part_2(data: str) -> int:
    rules, messages = data.strip().split("\n\n")
    rules = __get_rules(rules)
    middle_count = 0
    for message in messages.strip().split("\n"):
        message = eval(message)
        if not __check_message(message, rules):
            while not __check_message(message, rules):
                message = __fix_incorrect_message(message, rules)
            middle_count += int(message[len(message) // 2])
    return middle_count

def main():
    data = []
    with open("5/data.txt", "r") as f:
        data = f.read()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
