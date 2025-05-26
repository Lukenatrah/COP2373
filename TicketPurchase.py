def get_ticket_request():
    """The max tickets a user can get is 4"""
    while True:
        try:
            tickets = int(input("How many tickets would you like to buy (1, 2, 3, 4)? "))
            if 1 <= tickets <= 4:
                return tickets
            else:
                print("Max ticket count is 4 per party.")
        except ValueError:
            print("Enter a value 1 through 4.")

def sell_tickets():
    total_tickets = 20
    buyers = 0 

    while total_tickets > 0:
        print(f"\nTickets remaining: {total_tickets}")
        request = get_ticket_request()

        if request <= total_tickets:
            total_tickets -= request
            buyers += 1
            print(f"{request} Ticket(s) purchased. {total_tickets} ticket(s) remaining.")
        else:
            print(f"Unable to complete request, only {total_tickets} ticket(s) left. Try again.")

    print(f"\nTickets sold! Total number of buyers: {buyers}")

sell_tickets()
