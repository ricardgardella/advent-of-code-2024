import pandas as pd

def part_1(df: pd.DataFrame) -> int:
    sorted_left = sorted(df["Left"])
    sorted_right = sorted(df["Right"])
    return sum(abs(left - right) for left, right in zip(sorted_left, sorted_right))

def part_2(df: pd.DataFrame) -> int:
    total_count = 0
    for i in range(len(df)):
        left = df.iloc[i]["Left"]
        count = df.loc[df["Right"] == left, "Right"].count() * left
        total_count += count
    return total_count

def main():
    df = pd.read_csv("data.csv", sep=",")
    print(part_1(df))
    print(part_2(df))
if __name__ == "__main__":
    main()
