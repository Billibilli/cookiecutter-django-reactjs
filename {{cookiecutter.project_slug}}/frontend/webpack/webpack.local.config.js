var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
var webpack = require('webpack');
var config = require('./webpack.base.config.js');

config.entry = {
  main: [
    'react-hot-loader/patch',
    'webpack-dev-server/client?http://0.0.0.0:3000',
    'webpack/hot/only-dev-server',
    path.join(__dirname, '../js/src/main/index')
  ]
};

config.devtool = 'eval';
config.output = {
  path: path.join(__dirname, '../js/builds-dev/'),
  filename: '[name]-[hash].js',
  publicPath: 'http://0.0.0.0:3000/js/builds/',
};

config.plugins = [
  new webpack.HotModuleReplacementPlugin(),
  new BundleTracker({ filename: './frontend/webpack/webpack-stats.dev.json' }),
  new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('development'),
      BASE_URL: JSON.stringify('http://0.0.0.0:8000/'),
    }
  })
];

config.devServer = {
  inline: true,
  hot: true,
  historyApiFallback: true,
  host: '0.0.0.0',
  port: 3000,
  headers: { 'Access-Control-Allow-Origin': '*' }
};

module.exports = config;
