// Tiệm Heroes — văn phòng pixel. Chạy: node tiem/server.js  → mở http://localhost:4747
// Không cần cài thư viện. Chỉ đọc file trạng thái, không gửi dữ liệu ra ngoài.
const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const PORT = process.env.TIEM_PORT || 4747;
const HOST = process.env.TIEM_HOST || '127.0.0.1'; // chỉ máy này xem được; sau dùng Tailscale
const STATUS = process.env.TIEM_STATUS || path.join(os.homedir(), '.tiem-heroes', 'status.json');
const INDEX = path.join(__dirname, 'index.html');

function readStatus() {
  try { return JSON.parse(fs.readFileSync(STATUS, 'utf8')); }
  catch { return { agents: {}, hero_online: false, note: 'chưa có status.json' }; }
}

http.createServer((req, res) => {
  if (req.url.startsWith('/status.json')) {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
    return res.end(JSON.stringify(readStatus()));
  }
  if (req.url === '/favicon.ico') { res.writeHead(204); return res.end(); }
  if (req.url === '/' || req.url.startsWith('/index.html')) {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    return fs.createReadStream(INDEX).pipe(res);
  }
  res.writeHead(404); res.end('not found');
}).listen(PORT, HOST, () => console.log(`☕ Tiệm Heroes mở cửa: http://${HOST}:${PORT}  (trạng thái: ${STATUS})`));
