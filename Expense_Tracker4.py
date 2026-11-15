
def main():
    total_spent = 0.0
    expense_count = 0

    print("=" * 42)
    print("             MY EXPENSE TRACKER")
    print("=" * 42)
    print("Enter one expense amount at a time.")
    print("Type 'done' or 'quit' when you have finished.\n")

    while True:
        user_entry = input("Enter expense amount (or done): ").strip()

        if user_entry.lower() in ("done", "quit"):
            break

        try:
            expense = float(user_entry)

            if expense <= 0:
                print("Please enter an amount greater than zero.\n")
                continue

            total_spent += expense
            expense_count += 1
            print(f"Added: Rs. {expense:.2f}")
            print(f"Current total: Rs. {total_spent:.2f}\n")

        except ValueError:
            print("Invalid input. Please enter a number, such as 150 or 49.50.\n")

    print("\n" + "=" * 42)
    print("               EXPENSE SUMMARY")
    print("=" * 42)
    print(f"Number of expenses : {expense_count}")
    print(f"Total amount spent : Rs. {total_spent:.2f}")
    print("=" * 42)
    print("Thank you for using My Expense Tracker!")


if __name__ == "__main__":
    main()