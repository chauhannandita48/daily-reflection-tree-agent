def reflection_agent():
    print("---- Daily Reflection Agent ----\n")

    score = 0

    tasks = input("Did you complete your tasks? (yes/no): ").lower()
    if tasks == "yes":
        score += 1
    else:
        reason = input("Why not? (time/distraction/motivation): ")
        print(f"👉 Action: Improve {reason}")

    learning = input("\nDid you learn something new? (yes/no): ").lower()
    if learning == "yes":
        score += 1
    else:
        print("👉 Action: Allocate time for learning")

    health = input("\nDid you maintain your health? (yes/no): ").lower()
    if health == "yes":
        score += 1
    else:
        print("👉 Action: Improve sleep/diet/exercise")

    focus = input("\nWere distractions minimized? (yes/no): ").lower()
    if focus == "yes":
        score += 1
    else:
        print("👉 Action: Reduce distractions")

    print("\n---- FINAL RESULT ----")

    if score == 4:
        print("✅ Productive Day")
    elif score >= 2:
        print("⚖️ Average Day")
    else:
        print("❌ Unproductive Day")


if __name__ == "__main__":
    reflection_agent()
