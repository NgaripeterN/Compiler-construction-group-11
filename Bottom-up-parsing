class Parser:
    def __init__(self, grammar):
        self.grammar = grammar  # Grammar rules
        self.stack = []  # Parsing stack
        self.input = []  # Input tokens

    def parse(self, tokens):
        self.input = tokens + ["$"]  # Add end-of-input marker
        self.stack = ["$"]  # Initialize stack with end marker
        print(f"Initial stack: {self.stack}, Input: {self.input}")
        
        while True:
            action = self.next_action()
            if action == "SHIFT":
                self.shift()
            elif action.startswith("REDUCE"):
                rule_number = int(action.split()[1])
                self.reduce(rule_number)
            elif action == "ACCEPT":
                print("Parsing complete. Input accepted.")
                return True
            else:
                print(f"Error: Unexpected input. Stack: {self.stack}, Input: {self.input}")
                return False

    def next_action(self):
        # Simple logic for demonstration; extend for more complex grammars
        if not self.input:
            return "ACCEPT"

        # Example handling for a simple grammar
        if self.stack[-1] == "id" and len(self.input) > 1 and self.input[1] in ["+", "*", "$"]:
            return "REDUCE 4"  # Reduce rule 4: E -> id
        elif self.stack[-1] == "E" and self.input[0] in ["+", "*"]:
            return "SHIFT"
        elif self.stack[-1] == "E" and self.input[0] == "$":
            return "ACCEPT"
        else:
            return "SHIFT"

    def shift(self):
        token = self.input.pop(0)  # Remove token from input
        self.stack.append(token)  # Push token onto stack
        print(f"Shifting '{token}' to stack. Current stack: {self.stack}")

    def reduce(self, rule_number):
        if rule_number == 4:
            # Example reduction: E -> id
            if self.stack[-1] == "id":
                self.stack.pop()  # Remove 'id' from stack
                self.stack.append("E")  # Push 'E' to stack
                print(f"Reducing using rule 4: E -> id. Current stack: {self.stack}")

        # Add more rules here for your specific grammar
        # For demo, handling only the simple case of E -> id

# Sample grammar definition (simplified for demonstration)
grammar = {
    1: ["E", "E + E"],
    2: ["E", "E * E"],
    3: ["E", "( E )"],
    4: ["E", "id"]
}

# Create an instance of the parser with the grammar
parser = Parser(grammar)

# Example usage: Tokenized input representing a Zara program
tokens = ["id", "+", "id", "*", "id"]  # Represents: id + id * id

# Parse the input tokens
parser.parse(tokens)
