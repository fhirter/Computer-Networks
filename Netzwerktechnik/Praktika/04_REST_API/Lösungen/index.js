const express = require('express')
const app = express()
const port = 8080

const user = {
  name: "John Doe"
}

app.get('/users', (req, res) => {
  res.send(user);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})