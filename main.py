from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculator import RPNCalculator

app = FastAPI(title="RPN Calculator API", description="A simple RPN calculator API")

calculator = RPNCalculator()


class PushItem(BaseModel):
    value: float


@app.post("/rpn/stack", summary="Create a new stack")
async def create_stack():
    """
    Create a new stack with a unique identifier.

    Returns:
        dict: A dictionary containing the stack_id of the newly created stack.
    """
    stack_id = f"stack_{len(calculator.list_stacks()) + 1}"
    try:
        calculator.create_stack(stack_id)
        return {"stack_id": stack_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/rpn/stack", summary="List the available stacks")
async def list_stacks():
    """
    List all available stacks.

    Returns:
        dict: A dictionary containing a list of all stack identifiers.
    """
    return {"stacks": calculator.list_stacks()}


@app.post("/rpn/stack/{stack_id}", summary="Push a new value to a stack")
async def push(stack_id: str, item: PushItem):
    """
    Push a new value onto the specified stack.

    Args:
        stack_id (str): The identifier of the stack.
        item (PushItem): The item containing the value to be pushed onto the stack.

    Returns:
        dict: A dictionary containing the updated stack.

    Raises:
        HTTPException: If the stack is not found.
    """
    try:
        calculator.push(stack_id, item.value)
        return {"stack": calculator.get_stack(stack_id)}
    except KeyError:
        raise HTTPException(status_code=404, detail="Stack not found")


@app.get("/rpn/stack/{stack_id}", summary="Get a stack")
async def get_stack(stack_id: str):
    """
    Retrieve the current state of the specified stack.

    Args:
        stack_id (str): The identifier of the stack.

    Returns:
        dict: A dictionary containing the current state of the stack.

    Raises:
        HTTPException: If the stack is not found.
    """
    try:
        return {"stack": calculator.get_stack(stack_id)}
    except KeyError:
        raise HTTPException(status_code=404, detail="Stack not found")


@app.delete("/rpn/stack/{stack_id}", summary="Delete a stack")
async def delete_stack(stack_id: str):
    """
    Delete the specified stack.

    Args:
        stack_id (str): The identifier of the stack to be deleted.

    Returns:
        dict: A message confirming deletion of the stack.

    Raises:
        HTTPException: If the stack is not found.
    """
    try:
        calculator.delete_stack(stack_id)
        return {"message": "Stack deleted"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Stack not found")


@app.post("/rpn/op/{op}/stack/{stack_id}", summary="Apply an operand to a stack")
async def operate(op: str, stack_id: str):
    """
    Apply an operation to the top two elements of the specified stack.

    Args:
        op (str): The operator to apply ('+', '-', '*', '/').
        stack_id (str): The identifier of the stack.

    Returns:
        dict: A dictionary containing the updated state of the stack after operation.

    Raises:
        HTTPException: If there are insufficient operands or if division by zero occurs.
    """
    try:
        calculator.operate(stack_id, op)
        return {"stack": calculator.get_stack(stack_id)}
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)