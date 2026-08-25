/* Vanty Care — service worker (PWA + Push) */
const CACHE = 'vanty-care-v49-push';
const PRECACHE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './vanty-logo-icon.png',
  './vanty-favicon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(PRECACHE).catch(() => {})).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    caches.match(req).then((cached) => {
      const fetchPromise = fetch(req)
        .then((res) => {
          if (res && res.ok && url.pathname.match(/\.(html|js|css|png|webmanifest|svg|woff2?)$/i)) {
            const clone = res.clone();
            caches.open(CACHE).then((c) => c.put(req, clone));
          }
          return res;
        })
        .catch(() => cached);
      return cached || fetchPromise;
    })
  );
});

/** Push remoto (quando o servidor envia payload JSON) */
self.addEventListener('push', (event) => {
  let data = { title: 'Vanty Care', body: 'Tens uma atualização.', url: './index.html', tag: 'vanty-generic' };
  try {
    if (event.data) {
      const j = event.data.json();
      data = { ...data, ...j };
    }
  } catch (_) {
    try {
      const t = event.data && event.data.text();
      if (t) data.body = t;
    } catch (_) {}
  }
  event.waitUntil(
    self.registration.showNotification(data.title || 'Vanty Care', {
      body: data.body || '',
      icon: './vanty-logo-icon.png',
      badge: './vanty-favicon.png',
      tag: data.tag || 'vanty-generic',
      renotify: true,
      data: { url: data.url || './index.html' },
      vibrate: [80, 40, 80]
    })
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const target = (event.notification.data && event.notification.data.url) || './index.html';
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((list) => {
      for (const c of list) {
        if (c.url.includes(self.location.origin) && 'focus' in c) {
          c.postMessage({ type: 'VANTY_NOTIFICATION_CLICK', url: target });
          return c.focus();
        }
      }
      if (clients.openWindow) return clients.openWindow(target);
    })
  );
});

/** Mensagens da app (notificação local via SW) */
self.addEventListener('message', (event) => {
  const msg = event.data || {};
  if (msg.type === 'SHOW_NOTIFICATION') {
    event.waitUntil(
      self.registration.showNotification(msg.title || 'Vanty Care', {
        body: msg.body || '',
        icon: './vanty-logo-icon.png',
        badge: './vanty-favicon.png',
        tag: msg.tag || 'vanty-local',
        renotify: !!msg.renotify,
        data: { url: msg.url || './index.html' }
      })
    );
  }
  if (msg.type === 'SKIP_WAITING') self.skipWaiting();
});
