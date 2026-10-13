# Diseños Esme — deploy-ready

Este repo contiene los archivos mínimos para desplegar la PWA "Diseños Esme" en Vercel.

Archivos incluidos:
- index.html
- manifest.webmanifest
- sw.js
- icons/icon-192.svg
- icons/icon-512.svg
- icons/apple-touch-icon.svg

Notas importantes antes de desplegar en Vercel:
1. Chrome (Android) recomienda usar PNGs en el manifest (192x192 y 512x512). Actualmente el repo incluye SVGs como placeholder: convierte los SVGs a PNGs y sobreescribe en `/icons/` con los nombres `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`.
2. Después de deployar en Vercel, haz un hard refresh y verifica en DevTools → Application:
   - Manifest (debe decir "This page is installable")
   - Service Worker (debe estar registrado y "controlled")
3. Si no aparece el banner de instalación en Android, prueba abrir el menú del navegador (⋮) → "Install app" o "Add to home screen".

Cómo desplegar en Vercel:
- Conecta el repo a Vercel o importa el proyecto desde GitHub y haz Deploy.

Si querés, puedo generar los PNGs y subirlos al repo para dejarlo 100% listo — decime si querés que lo haga.