const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const jewelryApi = require('./api/jewelry');

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static('public'));
app.use('/api/jewelry', jewelryApi);

// Timer API
app.get('/api/time', (req, res) => {
    res.json({ time: new Date().toLocaleTimeString() });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
