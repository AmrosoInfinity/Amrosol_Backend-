const { TOKEN_TTL_MS } = require('../config/cacheConfig');
const cache = new Map();

function setToken(userId, service, hashToken, token, ttlMs = TOKEN_TTL_MS) {
  const key = `${userId}:${service}:${hashToken}`;
  cache.set(key, token);

  // hapus otomatis setelah TTL
  setTimeout(() => {
    cache.delete(key);
  }, ttlMs);
}

function getToken(userId, service, hashToken) {
  return cache.get(`${userId}:${service}:${hashToken}`);
}

module.exports = { setToken, getToken };
