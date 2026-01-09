// Timer
function updateTimer() {
    const now = new Date();
    document.getElementById("timer").innerText = now.toLocaleTimeString();
}
setInterval(updateTimer, 1000);
updateTimer();

// Fetch & render table
function loadJewelry() {
    axios.get('/api/jewelry')
        .then(res => {
            const tableBody = document.getElementById("table-body");
            tableBody.innerHTML = "";
            res.data.forEach(item => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${item.id}</td>
                    <td>${item.name}</td>
                    <td>${item.type}</td>
                    <td>${item.price}</td>
                    <td>
                        <button class="btn btn-danger btn-sm" onclick="deleteItem('${item.id}')">Delete</button>
                    </td>
                `;
                tableBody.appendChild(tr);
            });
        })
        .catch(err => console.error(err));
}

// Add item
function addItem() {
    const id = document.getElementById("id").value.trim();
    const name = document.getElementById("name").value.trim();
    const type = document.getElementById("type").value.trim();
    const price = document.getElementById("price").value.trim();

    if (!name || !type || !price) {
        alert("Please fill Name, Type, and Price");
        return;
    }

    axios.post('/api/jewelry/add', { id, name, type, price })
        .then(res => {
            alert(res.data.message);
            document.getElementById("form").reset();
            loadJewelry();
        })
        .catch(err => {
            console.error(err);
            alert("Error adding item");
        });
}

// Delete item
function deleteItem(id) {
    axios.delete(`/api/jewelry/delete/${id}`)
        .then(res => {
            alert(res.data.message);
            loadJewelry();
        })
        .catch(err => {
            console.error(err);
            alert("Error deleting item");
        });
}

// Load table on page load
window.onload = loadJewelry;
