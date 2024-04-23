from InMemoryDB import InMemoryDB

def main():
    inmemoryDB = InMemoryDB()

    # Should return None, because A doesn't exist in the DB yet
    print("Get A:", inmemoryDB.get("A"))

    try:
        # Should throw an error because a transaction is not in progress
        inmemoryDB.put("A", 5)
    except Exception as e:
        print("Error:", str(e))

    # Starts a new transaction
    inmemoryDB.begin_transaction()

    # Sets value of A to 5, but it's not committed yet
    inmemoryDB.put("A", 5)

    # Should return None, because updates to A are not committed yet
    print("Get A:", inmemoryDB.get("A"))

    # Updates A's value to 6 within the transaction
    inmemoryDB.put("A", 6)

    # Commits the open transaction
    inmemoryDB.commit()

    # Should return 6, that was the last value of A to be committed
    print("Get A:", inmemoryDB.get("A"))

    try:
        # Throws an error, because there is no open transaction
        inmemoryDB.commit()
    except Exception as e:
        print("Error:", str(e))

    try:
        # Throws an error because there is no ongoing transaction
        inmemoryDB.rollback()
    except Exception as e:
        print("Error:", str(e))

    # Should return None because B does not exist in the database
    print("Get B:", inmemoryDB.get("B"))

    # Starts a new transaction
    inmemoryDB.begin_transaction()

    # Sets key B's value to 10 within the transaction
    inmemoryDB.put("B", 10)
    print("Get B:", inmemoryDB.get("B"))

    # Rollbacks the transaction - revert any changes made to B
    inmemoryDB.rollback()

    # Should return None because changes to B were rolled back
    print("Get B:", inmemoryDB.get("B"))

if __name__ == "__main__":
    main()