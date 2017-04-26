if (process.env.NODE_ENV === 'production') {
  module.exports = require('./ConfigureStore.production');
} else {
  module.exports = require('./ConfigureStore.development')
}
