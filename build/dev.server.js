var devMiddleware = require('webpack-dev-middleware')(compiler, {
  headers: {
    "Access-Control-Allow-Origin":"\*"
  },
})