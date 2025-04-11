# Example: Python

```python
import requests

resp = requests.get("http://localhost:8000/random-joke")
print(resp.json()["joke"])
```