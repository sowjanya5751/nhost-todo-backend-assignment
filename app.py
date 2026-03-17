import streamlit as st
st.caption("Built using Streamlit (Frontend) + Nhost GraphQL (Backend)")
st.title("📝 Todo Application")
st.write("Simple task manager with CRUD operations")

# Local temporary storage
if "todos" not in st.session_state:
    st.session_state.todos = []

# Add Task
st.subheader("Add Task")
task = st.text_input("Enter task")

if st.button("Add Task"):
    if task:
        st.session_state.todos.append({"title": task, "done": False})
        st.success("Task added!")

# Show Tasks
st.subheader("Tasks")

for i, todo in enumerate(st.session_state.todos):
    col1, col2, col3 = st.columns([4,1,1])

    col1.write(todo["title"])

    # Mark done
    if col2.button("✔", key=f"done_{i}"):
        st.session_state.todos[i]["done"] = True

    # Delete
    if col3.button("❌", key=f"delete_{i}"):
        st.session_state.todos.pop(i)
        st.rerun()

# Show status
for todo in st.session_state.todos:
    st.write(f"{todo['title']} - {'✅ Done' if todo['done'] else '❌ Pending'}")