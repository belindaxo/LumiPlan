const BASE_URL = 'http://localhost:5000';

// Fetch all tasks for a given user
export const fetchTasks = async (userId) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks/${userId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch tasks');
        }
        const tasks = await response.json();
        return tasks;
    } catch (error) {
        console.error('Error fetching tasks:', error);
        throw error;
    }
};

// Add a new task
export const addTask = async (task, userId) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ...task, user_id: userId }),
        });
        if (!response.ok) {
            throw new Error('Failed to add task');
        }
        const newTask = await response.json();
        return newTask;
    } catch (error) {
        console.error('Error adding task:', error);
        throw error;
    }
};

// Update an existing task
export const updateTask = async (task, taskId) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(task),
        });
        if (!response.ok) {
            throw new Error('Failed to update task');
        }
        const updatedTask = await response.json();
        return updatedTask;
    } catch (error) {
        console.error('Error updating task:', error);
        throw error;
    }
};

// Delete a task
export const deleteTask = async (taskId) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks/${taskId}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Failed to delete task');
        }
        return true; // Assuming deletion was successful, adjust as needed based on your API response
    } catch (error) {
        console.error('Error deleting task:', error);
        throw error;
    }
};

// Fetch a single task details
export const fetchTask = async (taskId) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks/single/${taskId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch task');
        }
        const task = await response.json();
        return task;
    } catch (error) {
        console.error('Error fetching task:', error);
        throw error;
    }
};
