const express = require('express');
const cors = require('cors');
const tokenRoutes = require('./routes/tokenRoutes');
const requestLogger = require('./middleware/requestLogger');

const app = express();

// middleware
app.use(cors());
app.use(express.json());
app.use(requestLogger);

// routes
app.use('/', tokenRoutes);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Amrosol Backend running on port ${PORT}`);
});
