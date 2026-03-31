const { getToken } = require('../services/tokenCache');

function fetchToken(req, res) {
  const { service, userId, hashToken } = req.params;
  const token = getToken(userId, service, hashToken);

  if (!token) {
    return res.status(404).json({ error: "Token tidak ditemukan atau sudah kadaluarsa" });
  }

  res.json({
    service,
    userId,
    token,
    ttl: "2 menit"
  });
}

module.exports = { fetchToken };
