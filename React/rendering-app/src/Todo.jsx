function TodoList () {
    const tasks=[
        {id:1,text:"Complete React assignmnet"},
        {id:2,text:"Complete Node assignment"},
        {id:3,text:"Complete CI/CD assignment"}
    ];
    return (
        <div>
            <h2>Todo List</h2>
            <ul>
                {tasks.map((task)=> (
                    <li key={task.id}>{task.text}</li>
                ))}

            </ul>

        </div>
    );
}
export default TodoList










