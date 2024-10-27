    # Zara program 
# // Variable declarations
# integer x = 10;
# float y = 20.5;
# string name = "Zara";
# array numbers = [1, 2, 3, 4];
# stack stackVar;

# // Function declaration
# void display() {
#     integer z = 5;
#     print("Displaying data");
# }

# // Main program
# void main() {
#     x = 15;
#     y = y * 2;
#     if (x > 10) {
#         display();
#     }
# }

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
        if name in self.table:
            print(f"Symbol '{name}' already exists. Updating symbol.")
            self.update_symbol(name, value)
        else:
            self.table[name] = Symbol(name, symbol_type, value, scope)

    def update_symbol(self, name, value):
        if name in self.table:
            self.table[name].value = value
        else:
            print(f"Symbol '{name}' not found. Cannot update.")

    def retrieve_symbol(self, name):
        return self.table.get(name, f"Symbol '{name}' not found.")

    def display_symbols(self):
        for name, symbol in self.table.items():
            print(symbol)

# Simulating parsing and adding entries to the symbol table
symbol_table = SymbolTable()

# Parsing Zara program (simulated)
# Global variables
symbol_table.add_symbol("x", "integer", 10)
symbol_table.add_symbol("y", "float", 20.5)
symbol_table.add_symbol("name", "string", "Zara")
symbol_table.add_symbol("numbers", "array", [1, 2, 3, 4])
symbol_table.add_symbol("stackVar", "stack")

# Function: display
symbol_table.add_symbol("display", "function", scope="global")
symbol_table.add_symbol("z", "integer", 5, scope="display")

# Main function
symbol_table.add_symbol("main", "function", scope="global")
symbol_table.update_symbol("x", 15)  # Updating x
symbol_table.update_symbol("y", 41.0)  # Updating y after multiplication

# Display all symbols to verify
print("\nSymbol Table Entries after Parsing:")
symbol_table.display_symbols()
