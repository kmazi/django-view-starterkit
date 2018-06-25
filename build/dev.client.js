// before
var hotClient = require('webpack-hot-middleware/client?noInfo=true&reload=true')
// after
var hotClient = require('webpack-hot-middleware/client?noInfo=true&reload=true&path=http://localhost:8080/__webpack_hmr')
