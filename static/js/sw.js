self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('store').then((cache) => cache.addAll([
      '/',
      '/hand/templates/index.html', //需要缓存的静态资源
    ])),
  );
});

self.addEventListener('fetch', (e) => {
  console.log(e.request.url);
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request)),
  );
});