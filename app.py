import streamlit as st
from typing import Callable

# Conversion functions

def length_conversion(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        "m": 1, "km": 0.001, "mi": 0.000621371, "ft": 3.28084, "in": 39.3701, 
        "cm": 100, "mm": 1000, "yd": 1.09361, "nmi": 0.000539957
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_conversion(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        "g": 1, "kg": 0.001, "lb": 0.00220462, "oz": 0.035274, "t": 0.000001,
        "mg": 1000, "st": 0.00015747
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_conversion(value: float, from_unit: str, to_unit: str) -> float:
    conversions = {
        "C_to_F": lambda c: (c * 9/5) + 32,
        "C_to_K": lambda c: c + 273.15,
        "C_to_R": lambda c: (c + 273.15) * 9/5,
        "F_to_C": lambda f: (f - 32) * 5/9,
        "F_to_K": lambda f: (f + 459.67) * 5/9,
        "F_to_R": lambda f: f + 459.67,
        "K_to_C": lambda k: k - 273.15,
        "K_to_F": lambda k: (k * 9/5) - 459.67,
        "K_to_R": lambda k: k * 9/5,
        "R_to_C": lambda r: (r - 491.67) * 5/9,
        "R_to_F": lambda r: r - 459.67,
        "R_to_K": lambda r: r * 5/9
    }
    if from_unit == to_unit:
        return value
    key = f"{from_unit}_to_{to_unit}"
    return conversions[key](value)

def time_conversion(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {
        "s": 1, "min": 1/60, "h": 1/3600, "d": 1/86400, "wk": 1/604800,
        "mo": 1/2.628e+6, "yr": 1/3.154e+7, "decades": 1/3.154e+8, "centuries": 1/3.154e+9
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# More conversion functions (speed, area, volume, etc.) can be added here in a similar structure.

def convert(value: float, from_unit: str, to_unit: str, conversion_function: Callable) -> float:
    """Handles conversion using the appropriate function."""
    try:
        return round(conversion_function(value, from_unit, to_unit), 6)
    except KeyError:
        return "Invalid unit selection"

def main():
    st.title("Multi-Category Unit Converter")
    st.markdown("### Convert units across multiple categories with ease!")
    
    categories = {
        "Length": (length_conversion, ["m", "km", "mi", "ft", "in", "cm", "mm", "yd", "nmi"]),
        "Weight/Mass": (weight_conversion, ["g", "kg", "lb", "oz", "t", "mg", "st"]),
        "Temperature": (temperature_conversion, ["C", "F", "K", "R"]),
        "Time": (time_conversion, ["s", "min", "h", "d", "wk", "mo", "yr", "decades", "centuries"]),
        # More categories can be added here.
    }
    
    category = st.selectbox("Select Category", list(categories.keys()))
    conversion_function, units = categories[category]
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        value = st.number_input("Enter Value", min_value=0.0, format="%f")
    with col2:
        from_unit = st.selectbox("From", units)
    with col3:
        to_unit = st.selectbox("To", units)
    
    if st.button("Convert"):
        result = convert(value, from_unit, to_unit, conversion_function)
        st.success(f"Converted Value: {result} {to_unit}")

if __name__ == "__main__":
    main()


