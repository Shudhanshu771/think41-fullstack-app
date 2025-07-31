package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/api/tasks")
@CrossOrigin(origins = "*")
public class TaskController {

    private List<Task> tasks = new ArrayList<>(List.of(
        new Task(1, "Build UI"),
        new Task(2, "Connect Backend"),
        new Task(3, "Test API")
    ));

    private int currentId = 4;

    @GetMapping
    public List<Task> getTasks() {
        return tasks;
    }

    @PostMapping
    public Task createTask(@RequestBody Task newTask) {
        newTask.setId(currentId++);
        tasks.add(newTask);
        return newTask;
    }

    @PutMapping("/{id}")
    public Task updateTask(@PathVariable int id, @RequestBody Task updatedTask) {
        for (Task t : tasks) {
            if (t.getId() == id) {
                t.setName(updatedTask.getName());
                return t;
            }
        }
        return null;
    }

    @DeleteMapping("/{id}")
    public void deleteTask(@PathVariable int id) {
        tasks.removeIf(t -> t.getId() == id);
    }
}
