import streamlit as st

def find_largest_number(a, b, c):
    """Function to find the largest number among three input values"""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="Largest Number Finder")

    # Create input fields for three numbers
    number1 = st.number_input("Enter Number 1:", value=0, step=1)
    number2 = st.number_input("Enter Number 2:", value=0, step=1)
    number3 = st.number_input("Enter Number 3:", value=0, step=1)

    # Call the find_largest_number function to determine the largest number
    largest_number = find_largest_number(number1, number2, number3)

    # Display the result
    st.write("The largest number is:", largest_number)

if __name__ == "__main__":
    main()
