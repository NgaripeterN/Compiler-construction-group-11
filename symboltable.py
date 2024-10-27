class Symbol:
    def __init__(self, name, symbol_type, value=None, scope="global"):
        self.name = name
        self.type = symbol_type
        self.value = value
        self.scope = scope

    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.type}, value={self.value}, scope={self.scope})"

class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_symbol(self, name, symbol_type, value=None, scope="global"):
        # Use a unique key by combining name and scope to handle scoped symbols
        key = (name, scope)
        if key in self.table:
            print(f"Symbol '{name}' in scope '{scope}' already exists. Updating symbol.")
            self.update_symbol(name, value, scope)
        else:
            self.table[key] = Symbol(name, symbol_type, value, scope)

    def update_symbol(self, name, value, scope="global"):
        key = (name, scope)
        if key in self.table:
            self.table[key].value = value
        else:
            print(f"Symbol '{name}' in scope '{scope}' not found. Cannot update.")

    def retrieve_symbol(self, name, scope="global"):
        key = (name, scope)
        return self.table.get(key, f"Symbol '{name}' in scope '{scope}' not found.")

    def display_symbols(self):
        for (name, scope), symbol in self.table.items():
            print(symbol)

# Initialize the symbol table
symbol_table = SymbolTable()

# Adding symbols as per a Zara-style program with scopes
symbol_table.add_symbol("x", "integer", 10)
symbol_table.add_symbol("y", "float", 20.5)
symbol_table.add_symbol("name", "string", "Zara")
symbol_table.add_symbol("numbers", "array", [1, 2, 3, 4])
symbol_table.add_symbol("stackVar", "stack")

# Adding a scoped variable (e.g., inside a function 'display')
symbol_table.add_symbol("z", "integer", 5, scope="display")

# Update a symbol in the global scope (simulating assignment)
symbol_table.update_symbol("x", 15)

# Retrieve and display a specific symbol in the 'display' function scope
print("Retrieved Symbol 'z' in scope 'display':", symbol_table.retrieve_symbol("z", scope="display"))

# Display all symbols to verify entries with scopes
print("\nAll Symbols in Symbol Table:")
symbol_table.display_symbols()
