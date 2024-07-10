import streamlit as st
st.title("Input values")
st.write("The folllowing sliders refers to how many pixels the T-Rex will jump before seeing the obstacle. Select each value to customize your own bot")

values=[]

values.append(st.slider(label="Under 10 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 10 and 20 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 20 and 30 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 30 and 40 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 40 and 60 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 60 and 80 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Between 80 and 100 seconds", min_value=50, max_value=300))
values.append(st.slider(label="Over 100 seconds", min_value=50, max_value=300))

st.subheader("Best values")
st.write("95  |  130  |  155  |  180  |  197  |  220  |  270  |  300")

with open("values.txt", "w") as file:
    for i in values:
        file.writelines(f"{i},")