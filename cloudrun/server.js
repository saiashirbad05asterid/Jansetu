import http from 'node:http';
import { verifyReportFlow, areaPolicyFlow } from './genkit.js';

const port = Number(process.env.PORT || 8080);
const projectId = process.env.FIREBASE_PROJECT_ID || 'playground-0505';

const readJson = (request) => new Promise((resolve, reject) => {
  let body = '';
  request.on('data', (chunk) => { body += chunk; if (body.length > 100000) reject(new Error('Payload too large')); });
  request.on('end', () => { try { resolve(JSON.parse(body || '{}')); } catch { reject(new Error('Invalid JSON')); } });
  request.on('error', reject);
});


const server = http.createServer((request, response) => {
  response.setHeader('Content-Type', 'application/json; charset=utf-8');
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  response.setHeader('Cache-Control', 'no-store');

  if (request.method === 'OPTIONS') { response.writeHead(204); response.end(); return; }

  if (request.method === 'GET' && request.url === '/health') {
    response.writeHead(200);
    response.end(JSON.stringify({ ok: true, service: 'jansetu-api', projectId }));
    return;
  }

  if (request.method === 'GET' && request.url === '/api/config') {
    response.writeHead(200);
    response.end(JSON.stringify({ projectId, auth: 'firebase', data: 'firestore', files: 'storage' }));
    return;
  }

  if (request.method === 'POST' && request.url === '/api/verify-report') {
    readJson(request).then(async (payload) => {
      const result = await verifyReportFlow({ description: String(payload.description || ''), location: String(payload.location || ''), state: String(payload.state || '') });
      response.writeHead(200); response.end(JSON.stringify(result));
    }).catch((error) => { response.writeHead(502); response.end(JSON.stringify({ error: error.message })); });
    return;
  }

  if (request.method === 'POST' && request.url === '/api/area-insights') {
    readJson(request).then(async (payload) => {
      const result = await areaPolicyFlow({ area: String(payload.area || 'India'), reports: (payload.reports || []).slice(0, 25) });
      response.writeHead(200); response.end(JSON.stringify(result));
    }).catch((error) => { response.writeHead(502); response.end(JSON.stringify({ error: error.message })); });
    return;
  }

  response.writeHead(404);
  response.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(port, '0.0.0.0', () => console.log(`JanSetu API listening on ${port}`));
