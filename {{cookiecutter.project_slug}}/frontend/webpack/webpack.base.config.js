var path = require('path');

module.exports = {

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: [['env', { modules: false }], 'stage-2', 'react']
            }
          }
        ]
      },
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      }
    ]
  },

  resolve: {
    modules: [
      path.join(__dirname, 'frontend/js/src'),
      'node_modules'
    ],
    extensions: ['.js', '.jsx']
  }
};
