// Change 'v1' to 'v2' to force an update
const CACHE_NAME = 'code-swiftly-v2'; 
const ASSETS = [
    './',
    './index.html',
    './manifest.json',
    // Add any local CSS or JS files here
];

self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
    );
});

// This part is CRITICAL: It deletes the old 'v1' cache
self.addEventListener('activate', (e) => {
    e.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            );
        })
    );
});

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((res) => res || fetch(e.request))
    );
});