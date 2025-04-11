# Example: JavaScript (Fetch API)

```js
fetch("http://localhost:8000/random-joke")
  .then(res => res.json())
  .then(data => console.log(data.joke));
```