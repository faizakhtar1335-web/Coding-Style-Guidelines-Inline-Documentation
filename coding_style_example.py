"""
Order service example demonstrating the team's Python coding standards.

This module provides small, readable functions for validating an order,
calculating its total, and describing the order. It is an educational
example and does not connect to a payment gateway or database.
"""

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class OrderItem:
    """Represent one item in an order.

    Attributes:
        name: Human-readable product name.
        unit_price: Price of one unit, expressed in the smallest currency unit.
        quantity: Number of units ordered.
    """

    name: str
    unit_price: int
    quantity: int


def validate_order(items: Sequence[OrderItem]) -> None:
    """Validate the items in an order.

    Raises:
        ValueError: If the order is empty or an item has invalid values.
    """
    if not items:
        raise ValueError("An order must contain at least one item.")

    for item in items:
        if not item.name.strip():
            raise ValueError("Each item must have a product name.")
        if item.unit_price < 0:
            raise ValueError("Item prices cannot be negative.")
        if item.quantity <= 0:
            raise ValueError("Item quantities must be greater than zero.")


def calculate_order_total(items: Sequence[OrderItem]) -> int:
    """Return the order total in the smallest currency unit.

    Args:
        items: Items that belong to the order.

    Returns:
        The sum of unit price multiplied by quantity for each item.

    Raises:
        ValueError: If the order contains invalid items.
    """
    validate_order(items)

    # Calculate each line total separately to keep the business rule explicit.
    return sum(item.unit_price * item.quantity for item in items)


def format_order_summary(items: Sequence[OrderItem]) -> str:
    """Create a concise, human-readable order summary."""
    total = calculate_order_total(items)
    item_count = sum(item.quantity for item in items)

    return (
        f"Order contains {item_count} item(s). "
        f"Total: {total} minor currency unit(s)."
    )


def main() -> None:
    """Run a small example when this file is executed directly."""
    sample_items = [
        OrderItem(name="Notebook", unit_price=500, quantity=2),
        OrderItem(name="Pen", unit_price=100, quantity=3),
    ]

    print(format_order_summary(sample_items))


if __name__ == "__main__":
    main()
