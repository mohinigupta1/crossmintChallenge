from apiRequests import create_cometh, create_soloon

VALID_DIRECTIONS = {"up", "down", "left", "right"}
VALID_COLORS = {"blue", "red", "purple", "white"}

def space_object_helper(cell, row, col, valid_values, create_fn, label):
    """Space object helper for extracting/validateing values and calling appropriate create functions."""

    if "_" not in cell:
        raise ValueError(f"invalid cell value '{cell}' for {label} at ({row}, {col})")
    value = cell.split("_")[0].lower()
    if value not in valid_values:
        raise ValueError(f"invalid {label.lower()} '{value}' at ({row}, {col})")
    create_fn(row, col, value)

def cometh_helper(cell, row, col):
    """Helper to create COMETH object."""
    space_object_helper(cell, row, col, VALID_DIRECTIONS, create_cometh, "COMETH")

def soloon_helper(cell, row, col): 
    """Helper to create SOLOON object."""
    space_object_helper(cell, row, col, VALID_COLORS, create_soloon, "SOLOON")