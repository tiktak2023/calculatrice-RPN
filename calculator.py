class RPNCalculator:
    """
    A class to represent an RPN (Reverse Polish Notation) calculator.
    """

    def __init__(self):
        """
        Initialize the RPNCalculator with an empty dictionary of stacks.
        """
        self.stacks = {}

    def create_stack(self, stack_id: str):
        """
        Create a new stack with the given identifier.

        Args:
            stack_id (str): The unique identifier for the stack.

        Raises:
            ValueError: If the stack already exists.
        """
        if stack_id in self.stacks:
            raise ValueError("Stack already exists")
        self.stacks[stack_id] = []

    def push(self, stack_id: str, value: float):
        """
        Push a value onto the specified stack.

        Args:
            stack_id (str): The identifier of the stack.
            value (float): The value to push onto the stack.

        Raises:
            ValueError: If the stack is not found.
        """
        if stack_id not in self.stacks:
            raise ValueError("Stack not found")
        self.stacks[stack_id].append(value)

    def pop(self, stack_id: str):
        """
        Pop a value from the specified stack.

        Args:
            stack_id (str): The identifier of the stack.

        Returns:
            float: The value popped from the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if not self.stacks[stack_id]:
            raise ValueError("Stack is empty")
        return self.stacks[stack_id].pop()

    def clear(self, stack_id: str):
        """
        Clear all values from the specified stack.

        Args:
            stack_id (str): The identifier of the stack.
        """
        self.stacks[stack_id].clear()

    def operate(self, stack_id: str, operator: str):
        """
        Apply an operation to the top two elements of the specified stack.

        Args:
            stack_id (str): The identifier of the stack.
            operator (str): The operation to perform ('+', '-', '*', '/').

        Raises:
            ValueError: If there are not enough operands or if division by zero occurs.
            ValueError: If an unknown operator is provided.
        """
        if len(self.stacks[stack_id]) < 2:
            raise ValueError("Not enough operands")

        b, a = self.pop(stack_id), self.pop(stack_id)

        if operator == '+':
            self.push(stack_id, a + b)
        elif operator == '-':
            self.push(stack_id, a - b)
        elif operator == '*':
            self.push(stack_id, a * b)
        elif operator == '/':
            if b == 0:
                raise ValueError("Division by zero")
            self.push(stack_id, a / b)
        else:
            raise ValueError("Unknown operator")

    def get_stack(self, stack_id: str):
        """
        Get the current state of the specified stack.

        Args:
            stack_id (str): The identifier of the stack.

        Returns:
            list: A copy of the current state of the stack.
        """
        return self.stacks.get(stack_id, [])

    def list_stacks(self):
        """
        List all available stacks.

        Returns:
            list: A list of all stack identifiers.
        """
        return list(self.stacks.keys())

    def delete_stack(self, stack_id: str):
        """
        Delete the specified stack.

        Args:
            stack_id (str): The identifier of the stack to delete.

        Raises:
            KeyError: If the stack is not found.
        """
        if stack_id in self.stacks:
            del self.stacks[stack_id]