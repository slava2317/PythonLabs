import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from math import sin, sqrt
import matplotlib

def first_func(x):
    return x ** 2

def second_func(x):
    return x ** 3

def two_func():
    x = np.linspace(0, 100, 1000)
    first_y = [first_func(i) for i in x]
    second_y = [second_func(i) for i in x]
    fig, ax1 = plt.subplots()

    ax1.plot(x, first_y, 'b-', label='Первая функция')
    ax1.set_xlabel('Ось Х')
    ax1.set_ylabel('Ось Y для первой функции')

    ax2 = ax1.twinx()
    ax2.plot(x, second_y, 'r-', label='Вторая функция')
    ax2.set_ylabel('Ось Y для второй функции')

    fig.legend(loc="upper left")
    plt.title("График двух функций")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    st.pyplot(fig)  

def create_clusters():
    first_cluster_x = np.random.normal(2, 0.5, 50)
    first_cluster_y = np.random.normal(2, 0.5, 50)

    second_cluster_x = np.random.normal(4, 0.5, 50)
    second_cluster_y = np.random.normal(4, 0.5, 50)

    third_cluster_x = np.random.normal(8, 0.5, 50)
    third_cluster_y = np.random.normal(8, 0.5, 50)

    plt.scatter(first_cluster_x, first_cluster_y, color='blue', marker='o')
    plt.scatter(second_cluster_x, second_cluster_y, color='red', marker='o')
    plt.scatter(third_cluster_x, third_cluster_y, color='green', marker='o')
    
    plt.title("График кластеров")
    plt.xlabel("X")
    plt.ylabel("Y")
    st.pyplot(plt)  

def create_circular_diag():
    vals = [21, 19, 38, 12, 10]
    labels = ["footbal", "race", "hockey", "ufc", "run"]
    
    plt.pie(vals, labels=labels, autopct='%1.1f%%')
    plt.title("Круговая диаграмма")
    st.pyplot(plt) 

def create_heatmap():
    matrix = np.random.rand(10, 10)
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    
    plt.title("Тепловая карта")
    st.pyplot(plt)  

def create_bar_char():
    x = np.arange(1, 8)
    y = np.random.randint(1, 20, size=7)
    
    _, ax = plt.subplots()
    bars = ax.barh(x, y)
    ax.bar_label(bars, label_type='center', fontsize=20)
    
    plt.title("Столбчатая диаграмма")
    st.pyplot(plt)  

def f(x, y):
    return sin(sqrt(x ** 2 + y ** 2))

def create_surface_plot():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    z = [f(x[i], y[i]) for i in range(len(x))]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')

    plt.title("3D поверхность")
    st.pyplot(fig)  

tasks = []

def create_task(title):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    return tasks[-1]

def get_tasks(completed=None):
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]

def update_task(task_id, completed):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = completed
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

st.title("Task Manager with Graphs")

st.header("Task Management")

task_title = st.text_input("Enter a new task")
if st.button("Create Task"):
    if task_title:
        new_task = create_task(task_title)
        st.success(f"Task created: {new_task['title']}")

st.subheader("Current Tasks")
completed_filter = st.checkbox("Show completed tasks only")
tasks_to_show = get_tasks(completed_filter)
for task in tasks_to_show:
    st.write(f"ID: {task['id']} - {task['title']} - Completed: {task['completed']}")

task_id_to_update = st.number_input("Enter task ID to mark as completed", min_value=1, step=1)
if st.button("Update Task as Completed"):
    task = update_task(task_id_to_update, True)
    if task:
        st.success(f"Task {task_id_to_update} marked as completed")
    else:
        st.error(f"Task {task_id_to_update} not found")

task_id_to_delete = st.number_input("Enter task ID to delete", min_value=1, step=1)
if st.button("Delete Task"):
    delete_task(task_id_to_delete)
    st.success(f"Task {task_id_to_delete} deleted")


st.header("Graphs")

graph_option = st.selectbox("Choose a graph to display", ["Two Functions", "Clusters", "Circular Diagram", "Heatmap", "Bar Chart", "3D Surface Plot"])

if graph_option == "Two Functions":
    two_func()
elif graph_option == "Clusters":
    create_clusters()
elif graph_option == "Circular Diagram":
    create_circular_diag()
elif graph_option == "Heatmap":
    create_heatmap()
elif graph_option == "Bar Chart":
    create_bar_char()
elif graph_option == "3D Surface Plot":
    create_surface_plot()

