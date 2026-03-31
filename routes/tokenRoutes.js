const express = require('express');
const { fetchToken } = require('../controllers/tokenController');

const router = express.Router();

// endpoint: /grab/:userId/:hashToken atau /gojek/:userId/:hashToken
router.get('/:service/:userId/:hashToken', fetchToken);

module.exports = router;
