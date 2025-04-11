# API Endpoints

## Get a Random Joke

- **Endpoint**: `/random-joke`
- **Method**: GET
- **Description**: Retourne une blague aleatoire.
- **Response**:
  ```json
  {
    "joke": "Pourquoi les canards ont-ils autant de plumes ? Pour couvrir leur derrière !"
  }
  ```

## Submit a Joke

- **Endpoint**: `/submit`
- **Method**: POST
- **Description**: Soumet une nouvelle blague.
- **Request Body**:
  ```json
  {
    "joke": "Votre blague ici"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Joke added!",
    "total": 4
  }
  ```
