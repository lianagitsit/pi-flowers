const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(`
  <html>
    <h1>Pi Flowers</h1>
    <hr />
    <h2>Liana Flower</h2>
    <ul>
      <li><a href="/button?pi=liana">Press Button</a></li>
      <li><a href="/light?pi=liana">Should I light up?</a></li>
    </ul>
    <h2>Eric Flower</h2>
    <ul>
      <li><a href="/button?pi=eric">Press Button</a></li>
      <li><a href="/light?pi=eric">Should I light up?</a></li>
    </ul>
    <hr />
    Made by <a href="https://github.com/lianagitsit">Liana</a> and <a href="https://github.com/eqmvii">Eric</a>
  </html>
  `);
});

app.get('/light', (req, res) => {
  console.log(req.query.pi);
  res.json({success: 'test', route: 'light', requester: req.query.pi});
});

app.get('/button', (req, res) => {
  console.log(req.query.pi);
  res.json({success: 'test', route: 'button', requester: req.query.pi});
});

app.listen(PORT, () => console.log(`Listening on port ${port}!`));
