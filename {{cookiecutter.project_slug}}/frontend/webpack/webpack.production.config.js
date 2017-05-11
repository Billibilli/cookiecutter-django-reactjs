var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.base.config.js');

config.entry = {
  main: [
    path.join(__dirname, '../js/src/main/index')
  ]
};

config.output = {
  path: path.join(__dirname, '../js/builds/'),
  filename: '[name]-[hash].min.js',
  publicPath: '/js/builds/'
};

config.plugins = [
  new BundleTracker({ filename: './frontend/webpack/webpack-stats.production.json' }),
  new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('production'),
      BASE_URL: JSON.stringify('http://0.0.0.0/'),
    }
  }),
  new webpack.LoaderOptionsPlugin({
    minimize: true
  }),
  new webpack.optimize.UglifyJsPlugin({
    mangle: false,
    sourcemap: true,
    compress: {
      warnings: true
    }
  })
];

module.exports = config;
