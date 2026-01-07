import streamlit





streamlit.title("Simple Calculator App By IBTASAM QAMAR ")
num1= streamlit.number_input("Enter first number")
num2= streamlit.number_input("Enter second number")
operation= streamlit.selectbox(
    "Choose which operationnnn",
    ["add", "subtraction", "multiply", "division"]
)
if streamlit.button("Calculate"):
    if operation == "add":
        result= num1+num2
        streamlit.success(f"Answer  {result}")
    elif operation== "subtraction":
        result =num1-num2
        streamlit.success(f"Answer {result}")
    elif operation =="multiply":
        result= num1*num2
        streamlit.success(f"answer  {result}")
    elif operation =="division":
        if num2 ==0:
            streamlit.error("division by zero is not possible ")
        else:
            result =num1/num2
            streamlit.success(f"Answer is : {result}")