from Person import Person
from Contract import Contract
from Client import Client

def main():
    p1 = Person("Cai", "Towson", "Jan 17th")
    print(p1)
    print()
    contract = Contract("000001", "Dear, ______. Please sign here ______ to acknowledge the details.")
    c1 = Client("Jwon","Baltimore", "Jan 1st", contract)
    print(c1)

main()