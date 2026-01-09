const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

const router = express.Router();
const filePath = path.join(__dirname, '..', 'data', 'jewelry.csv');

// READ CSV
router.get('/', (req, res) => {
    const results = [];
    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', row => results.push(row))
        .on('end', () => res.json(results))
        .on('error', err => res.status(500).json(err));
});

// ADD ITEM 
router.post('/add', (req, res) => {
    let { id, name, type, price } = req.body;

    if (!name || !type || !price) {
        return res.status(400).json({ message: "Name, type and price are required" });
    }

    // Generate ID if empty
    if (!id) {
        id = Date.now().toString(); // unique timestamp-based ID
    }

    const line = `\n${id},${name},${type},${price}`;
    fs.appendFile(filePath, line, err => {
        if (err) return res.status(500).json({ message: "Error writing CSV" });
        res.json({ message: "Item Added Successfully" });
    });
});

// DELETE ITEM
router.delete('/delete/:id', (req, res) => {
    const id = req.params.id;
    const rows = [];

    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', row => { if (row.id !== id) rows.push(row); })
        .on('end', () => {
            const header = "id,name,type,price";
            const lines = rows.map(r => `${r.id},${r.name},${r.type},${r.price}`).join('\n');
            fs.writeFile(filePath, header + '\n' + lines, err => {
                if (err) return res.status(500).json({ message: "Error deleting item" });
                res.json({ message: "Item Deleted Successfully" });
            });
        });
});

module.exports = router;
