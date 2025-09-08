import os

def compute_bonus(salary: int) -> int:
    return int(salary * 0.10)

def load_token() -> str:
    # Example of something a real app might have in env
    return os.getenv("DEMO_TOKEN", "")

if __name__ == "__main__":
    print("bonus_for_100000", compute_bonus(100000))
