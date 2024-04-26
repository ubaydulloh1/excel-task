# task

### run celery worker

```bash
celery -A core worker --loglevel=info
```

### run celery beat

```bash
celery -A core beat --loglevel=info
```
