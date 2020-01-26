const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

let lightStatus = {
  liana: false,
  eric: false
};

let piMatches = {
  liana: 'eric',
  eric: 'liana'
};

app.get('/', (req, res) => {
  res.send(`
  <html>
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="/frontend.js"></script>
    <h1>Pi Flowers</h1>
    <hr />
    <h2>Liana Flower</h2>
    <p><strong>Lit: </strong> <span id=liana>${lightStatus.liana}</span></p>
    <ul>
      <li><a href="/light?pi=liana&button=true">Press Button</a></li>
      <li><a href="/light?pi=liana&button=false">Should I light up?</a></li>
    </ul>
    <h2>Eric Flower</h2>
    <p><strong>Lit: </strong><span id=eric>${lightStatus.eric}</span></p>
    <ul>
      <li><a href="/light?pi=eric&button=true">Press Button</a></li>
      <li><a href="/light?pi=eric&button=false">Should I light up?</a></li>
    </ul>
    <hr />
    Made by <a href="https://github.com/lianagitsit">Liana</a> and <a href="https://github.com/eqmvii">Eric</a>
  </html>
  `);
});

app.get('/status', (_req, res) => {
  res.json(lightStatus);
})

// Determine if the pi should light up, then reset status to false.
// If the button has been pressed, tell the other pi to light up.
app.get('/light', (req, res) => {
  let requestingPi = req.query.pi;
  let buttonPressed = (req.query.button == 'true');
  console.log(`@ @ @ @ @ @ @ @ Poll from ${requestingPi}. buttonPressed: ${buttonPressed}`);

  let shouldLight = lightStatus[requestingPi];

  if (shouldLight) {
    lightStatus[requestingPi] = false;
  }

  if (buttonPressed) {
    lightStatus[piMatches[requestingPi]] = true;
  }

  res.json({
    route: 'light',
    requester: requestingPi,
    shouldLight: shouldLight
  });
});

// DEPRECATED -- used to be an additional request for the button press
// Tell the other pi to light up the next time it polls /light
// app.get('/button', (req, res) => {
//   let requestingPi = req.query.pi;
//   console.log(`button press received from ${requestingPi}`);

//   // Set the OTHER pi's lightStatus to true
//   lightStatus[piMatches[requestingPi]] = true;

//   res.json({
//     route: 'button',
//     requester: requestingPi
//   });
// });

// Serve static files from the /public directory
app.use(express.static('public'))

app.listen(PORT, () => console.log(`Listening on port ${PORT}!`));
