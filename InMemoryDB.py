class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.transaction_data = {}
        self.transaction_active = False

    def get(self, key):
        if key in self.transaction_data:
            return self.transaction_data[key]
        elif key in self.db:
            return self.db[key]
        else:
            return None

    def put(self, key, val):
        if not self.transaction_active:
            raise Exception("No transaction in progress")
        self.transaction_data[key] = val

    def begin_transaction(self):
        if self.transaction_active:
            raise Exception("A transaction is already in progress")
        self.transaction_active = True
        self.transaction_data = {}

    def commit(self):
        if not self.transaction_active:
            raise Exception("No transaction in progress")
        self.db.update(self.transaction_data)
        self.transaction_data = {}
        self.transaction_active = False

    def rollback(self):
        if not self.transaction_active:
            raise Exception("No transaction in progress")
        self.transaction_data = {}
        self.transaction_active = False