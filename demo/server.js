const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());
app.use(express.json())
var getPixels = require("get-pixels")

 

app.use('/', (req, res) => {
    getPixels("out.png", function(err, pixels) {
        if(err) {
          console.log("Bad image path")
          return
        }
        console.log("got pixels", pixels.shape.slice())
        console.log(pixels.data)
        res.send(pixels.data);
      })
    
    console.log(req.body)
})
  


app.listen(8080, () => console.log('API is running on http://localhost:8080/login'));