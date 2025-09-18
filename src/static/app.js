document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const teamListDiv = document.getElementById('team-list');
    const taskListDiv = document.getElementById('task-list');
    const addMemberBtn = document.getElementById('add-member-btn');
    const addTaskBtn = document.getElementById('add-task-btn');
    const generateTasksBtn = document.getElementById('generate-tasks-btn');
    const memberNameInput = document.getElementById('member-name');
    const memberRoleInput = document.getElementById('member-role');
    const taskAssigneeSelect = document.getElementById('task-assignee');
    const taskDescriptionInput = document.getElementById('task-description');
    const aiTaskInput = document.getElementById('ai-task-input');
    const aiSpinner = document.getElementById('ai-spinner');
    const aiResultsDiv = document.getElementById('ai-results');

    // --- State ---
    let members = [];

    // --- API Functions ---
    const fetchData = async () => {
        try {
            const response = await fetch('/api/data');
            const data = await response.json();
            renderTeam(data.teams);
            renderTasks(data.tasks);
            updateAssigneeDropdown(data.teams);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const addMember = async () => {
        const name = memberNameInput.value.trim();
        const role = memberRoleInput.value.trim();
        if (!name || !role) {
            alert('Please enter both name and role.');
            return;
        }

        await fetch('/api/members', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, role }),
        });
        memberNameInput.value = '';
        memberRoleInput.value = '';
        fetchData();
    };

    const assignTask = async () => {
        const name = taskAssigneeSelect.value;
        const task = taskDescriptionInput.value.trim();
        if (!name || !task) {
            alert('Please select an assignee and enter a task.');
            return;
        }

        await fetch('/api/assignments', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, task }),
        });
        taskDescriptionInput.value = '';
        fetchData();
    };

    const removeMember = async (name) => {
        if (!confirm(`Are you sure you want to remove ${name}? This will also delete all their tasks.`)) {
            return;
        }
        await fetch(`/api/members/${name}`, { method: 'DELETE' });
        fetchData();
    };

    const generateSubtasks = async () => {
        const taskDescription = aiTaskInput.value.trim();
        if (!taskDescription) {
            alert('Please enter a high-level task.');
            return;
        }

        aiSpinner.style.display = 'block';
        aiResultsDiv.innerHTML = '';
        generateTasksBtn.disabled = true;

        try {
            const response = await fetch('/api/tasks/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ task_description: taskDescription }),
            });
            const data = await response.json();
            renderAISuggestions(data.subtasks);
        } catch (error) {
            console.error('Error generating tasks:', error);
            aiResultsDiv.innerHTML = '<p style="color: red;">Failed to generate tasks.</p>';
        } finally {
            aiSpinner.style.display = 'none';
            generateTasksBtn.disabled = false;
        }
    };
    
    // --- Render Functions ---
    const renderTeam = (teams) => {
        teamListDiv.innerHTML = '';
        for (const role in teams) {
            const roleEl = document.createElement('div');
            roleEl.innerHTML = `<h3>${role}</h3>`;
            const memberList = document.createElement('ul');
            teams[role].forEach(name => {
                const li = document.createElement('li');
                li.textContent = name;
                const deleteBtn = document.createElement('button');
                deleteBtn.textContent = '❌';
                deleteBtn.className = 'delete-btn';
                deleteBtn.onclick = () => removeMember(name);
                li.appendChild(deleteBtn);
                memberList.appendChild(li);
            });
            roleEl.appendChild(memberList);
            teamListDiv.appendChild(roleEl);
        }
    };

    const renderTasks = (tasks) => {
        taskListDiv.innerHTML = '';
        for (const name in tasks) {
            const assigneeEl = document.createElement('div');
            assigneeEl.innerHTML = `<h3>${name}</h3>`;
            const taskList = document.createElement('ul');
            if (tasks[name].length > 0) {
                tasks[name].forEach(task => {
                    const li = document.createElement('li');
                    li.textContent = task;
                    taskList.appendChild(li);
                });
            } else {
                 const li = document.createElement('li');
                 li.textContent = '(No tasks assigned)';
                 li.style.fontStyle = 'italic';
                 li.style.color = '#777';
                 taskList.appendChild(li);
            }
            assigneeEl.appendChild(taskList);
            taskListDiv.appendChild(assigneeEl);
        }
    };

    const updateAssigneeDropdown = (teams) => {
        taskAssigneeSelect.innerHTML = '<option value="">Select Member</option>';
        members = [];
        for (const role in teams) {
            teams[role].forEach(name => {
                if (!members.includes(name)) {
                    members.push(name);
                }
            });
        }
        members.sort().forEach(name => {
            const option = document.createElement('option');
            option.value = name;
            option.textContent = name;
            taskAssigneeSelect.appendChild(option);
        });
    };
    
    const renderAISuggestions = (subtasks) => {
        aiResultsDiv.innerHTML = '<h4>Suggested Sub-tasks:</h4>';
        if (!subtasks || subtasks.length === 0) {
            aiResultsDiv.innerHTML += '<p>No suggestions available.</p>';
            return;
        }
        subtasks.forEach(task => {
            const item = document.createElement('div');
            item.className = 'ai-task-item';
            
            const text = document.createElement('span');
            text.textContent = task;
            
            const addButton = document.createElement('button');
            addButton.textContent = 'Add Task';
            addButton.className = 'add-ai-task-btn';
            addButton.onclick = async () => {
                // Assign to the currently selected person or a default
                const selectedAssignee = taskAssigneeSelect.value;
                 if (!selectedAssignee) {
                    alert('Please select a member in the "Assign New Task" form first to add this task.');
                    return;
                }
                await fetch('/api/assignments', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: selectedAssignee, task: task }),
                });
                item.remove(); // Remove suggestion after adding
                fetchData();
            };

            item.appendChild(text);
            item.appendChild(addButton);
            aiResultsDiv.appendChild(item);
        });
    };

    // --- Event Listeners ---
    addMemberBtn.addEventListener('click', addMember);
    addTaskBtn.addEventListener('click', assignTask);
    generateTasksBtn.addEventListener('click', generateSubtasks);

    // --- Initial Load ---
    fetchData();
});