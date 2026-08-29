from typing import Union

def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculates the discounted price based on explicit type specifications (type hints)
    and a runtime check for a business rule (discount percentage range).
    """
    # This is a runtime check for a business rule. A more advanced static analyzer
    # with custom rules *could* potentially flag literal values outside this range.
    if not (0 <= discount_percentage <= 100):
        raise ValueError(f"Discount percentage must be between 0 and 100, got {discount_percentage}.")

    discount_factor = discount_percentage / 100.0
    discounted_price = original_price * (1 - discount_factor)
    return discounted_price

print("--- Demonstrating Static Analysis Concepts ---")

# Case 1: Correct usage, adheres to all specifications (types and business rules).
# A static analyzer (like mypy) would find no issues here.
print("\n--- Case 1: Correct Usage ---")
price_ok = calculate_discounted_price(100.0, 10.0)
print(f"Calculated price (100.0, 10.0%): {price_ok}")

# Case 2: Type Mismatch - Violates explicit type specification.
# A static analyzer (like mypy) *would* flag this call as an error
# because "300.0" is a string, but 'original_price' expects a float.
# If run without static analysis, this will cause a TypeError at runtime.
print("\n--- Case 2: Type Mismatch (Static Analysis Catches This) ---")
invalid_price_str: str = "300.0" # Explicitly typed as str
try:
    # mypy would report: Argument "original_price" to "calculate_discounted_price" has incompatible type "str"; expected "float"
    price_type_error = calculate_discounted_price(invalid_price_str, 15.0)
    print(f"Calculated price (invalid_price_str, 15.0%): {price_type_error}")
except TypeError as e:
    print(f"Runtime Error (as expected): {e}")

# Case 3: Value Out of Range - Adheres to types but violates a business rule.
# A basic static analyzer (like mypy) *might not* catch this, as 200.0 is a valid float.
# This highlights where static analysis based purely on types can be insufficient,
# and where "assumptions" about value ranges might lead to runtime issues.
# More advanced static analysis or custom rules would be needed to catch this statically.
print("\n--- Case 3: Value Out of Range (Basic Static Analysis Might Miss This) ---")
try:
    price_value_error = calculate_discounted_price(50.0, 200.0) # 200% discount is out of business spec
    print(f"Calculated price (50.0, 200.0%): {price_value_error}")
except ValueError as e:
    print(f"Runtime Error (as expected): {e}")

# Case 4: Potential None - Violates explicit type specification.
# A static analyzer (like mypy) *would* flag this call as an error
# because None is not a float. This prevents a common runtime bug.
print("\n--- Case 4: Potential None (Static Analysis Catches This) ---")
optional_discount: Union[float, None] = None # Explicitly typed as Union[float, None]
try:
    # mypy would report: Argument "discount_percentage" to "calculate_discounted_price" has incompatible type "None"; expected "float"
    price_none_error = calculate_discounted_price(100.0, optional_discount)
    print(f"Calculated price (100.0, None%): {price_none_error}")
except (TypeError, ValueError) as e: # None will cause a TypeError when multiplied, not ValueError from the function.
    print(f"Runtime Error (as expected): {e}")

print("\n--- Summary ---")
print("This example demonstrates how static analysis, particularly type checking,")
print("helps enforce explicit specifications (like type hints) in code.")
print("It catches potential bugs (e.g., type mismatches, None values) before runtime.")
print("However, it also shows that some 'assumptions' or complex business rules (like value ranges)")
print("might require more sophisticated static analysis rules or remain runtime checks,")
print("highlighting the balance between specification, static analysis, and runtime validation.")
