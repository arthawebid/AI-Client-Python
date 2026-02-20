# AI Client Python

Template ini sudah siap untuk:

* ✅ Environment config (.env)
* ✅ Logging production
* ✅ Gunicorn WSGI
* ✅ Error handling clean
* ✅ Health check endpoint
* ✅ Structured response
* ✅ Siap reverse proxy Nginx

---

# 📁 Struktur Project Production

```
ai-service/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ai_client.py
│   └── config.py
│
├── logs/
│
├── .env
├── requirements.txt
├── gunicorn.conf.py
├── run.py
└── README.md
```

# 🚀 Production Run (Ubuntu)

## Install

```
pip install -r requirements.txt
```

## Run with Gunicorn

```
gunicorn -c gunicorn.conf.py run:app
```

---

# 🔥 Setup systemd Service (Enterprise Standard)

File:

```
/etc/systemd/system/ai-service.service
```

```
[Unit]
Description=AI Service Production
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/ai-service
ExecStart=/var/www/ai-service/venv/bin/gunicorn -c gunicorn.conf.py run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable:

```
sudo systemctl daemon-reload
sudo systemctl enable ai-service
sudo systemctl start ai-service
```

---

# 🌐 Reverse Proxy Nginx

```
server {
    listen 80;
    server_name ai.local;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

# 🛡 Production Features Included

| Feature         | Status |
| --------------- | ------ |
| ENV Config      | ✅      |
| Logging         | ✅      |
| Error Handling  | ✅      |
| Health Check    | ✅      |
| Gunicorn WSGI   | ✅      |
| systemd service | ✅      |
| Nginx ready     | ✅      |

---

