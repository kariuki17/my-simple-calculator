
import streamlit as st

def calculator(num1, num2, operator):
    # Perform calculation based on operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        result = num1 / num2
    else:
        return "Error: Invalid operator!"
    
    return f"The result is: {result}"

def main():
    # Set page title
    st.title("Simple Calculator App")
    
    # Create input fields
    num1 = st.number_input("Enter the first number", step=0.1)
    num2 = st.number_input("Enter the second number", step=0.1)
    
    # Create operator selection
    operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])
    
    # Calculate button
    if st.button("Calculate"):
        result = calculator(num1, num2, operator)
        st.write(result)
    
    # Add some styling and information
    st.markdown("""
    ### Instructions:
    1. Enter two numbers
    2. Select an operator
    3. Click 'Calculate' to see the result
    """)

if __name__ == "__main__":
    main()
