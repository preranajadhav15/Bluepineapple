const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

const router = express.Router();
const csvPath = path.join(__dirname, '../data/jewelry.csv');

// READ
router.get('/all', (req, res) => {
    const items = [];
    fs.createReadStream(csvPath)
        .pipe(csv())
        .on('data', data => items.push(data))
        .on('end', () => res.json(items));
});

// ADD
router.post('/add', (req, res) => {
    const { id, name, type, price } = req.body;
    if (!id || !name || !type || !price) {
        return res.status(400).send('All fields required');
    }

    const line = `${id},${name},${type},${price}\n`;

    fs.appendFile(csvPath, line, err => {
        if (err) return res.status(500).send('Write failed');
        res.send('Item added successfully');
    });
});

// DELETE
router.delete('/delete/:id', (req, res) => {
    const deleteId = req.params.id;
    const items = [];

    fs.createReadStream(csvPath)
        .pipe(csv())
        .on('data', data => {
            if (data.id !== deleteId) items.push(data);
        })
        .on('end', () => {
            let out = 'id,name,type,price\n';
            items.forEach(i => out += `${i.id},${i.name},${i.type},${i.price}\n`);

            fs.writeFile(csvPath, out, err => {
                if (err) return res.status(500).send('Delete failed');
                res.send('Item deleted successfully');
            });
        });
});

// EDIT ITEM
router.put('/edit/:id', (req, res) => {
    const editId = req.params.id;
    const { name, type, price } = req.body;

    const items = [];

    fs.createReadStream(csvPath)
        .pipe(csv())
        .on('data', data => {
            if (data.id === editId) {
                data.name = name;
                data.type = type;
                data.price = price;
            }
            items.push(data);
        })
        .on('end', () => {
            let out = 'id,name,type,price\n';
            items.forEach(i => out += `${i.id},${i.name},${i.type},${i.price}\n`);

            fs.writeFile(csvPath, out, err => {
                if (err) return res.status(500).send('Update failed');
                res.send('Item updated successfully');
            });
        });
});


module.exports = router;
