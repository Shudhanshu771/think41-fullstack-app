import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTaskName, setNewTaskName] = useState("");
  const [editId, setEditId] = useState(null);
  const [editText, setEditText] = useState("");

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = () => {
    axios.get("http://localhost:8080/api/tasks").then((res) => {
      setTasks(res.data);
    });
  };

  const addTask = () => {
    if (!newTaskName.trim()) return;
    axios.post("http://localhost:8080/api/tasks", { name: newTaskName }).then(() => {
      setNewTaskName("");
      fetchTasks();
    });
  };

  const deleteTask = (id) => {
    axios.delete(`http://localhost:8080/api/tasks/${id}`).then(() => {
      fetchTasks();
    });
  };

  const startEdit = (task) => {
    setEditId(task.id);
    setEditText(task.name);
  };

  const saveEdit = () => {
    axios.put(`http://localhost:8080/api/tasks/${editId}`, { name: editText }).then(() => {
      setEditId(null);
      setEditText("");
      fetchTasks();
    });
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Think41 Task App</h1>
      <h2>Task List</h2>

      <input
        placeholder="Add new task"
        value={newTaskName}
        onChange={(e) => setNewTaskName(e.target.value)}
      />
      <button onClick={addTask}>Add</button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {editId === task.id ? (
              <>
                <input
                  value={editText}
                  onChange={(e) => setEditText(e.target.value)}
                />
                <button onClick={saveEdit}>Save</button>
              </>
            ) : (
              <>
                {task.name}
                <button onClick={() => startEdit(task)}>Edit</button>
                <button onClick={() => deleteTask(task.id)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
