package com.example.demo;

public class Task {
    private int id;
    private String name;

    // Constructor
    public Task(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // Empty constructor for JSON (important!)
    public Task() {}

    // Getters
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }


    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }
}
