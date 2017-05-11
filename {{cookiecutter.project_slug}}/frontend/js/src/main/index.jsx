import React from 'react';
import ReactDOM from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import { browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';

import Root from './Root';
import configureStore from './Store';


const store = configureStore();
const history = syncHistoryWithStore(browserHistory, store);


const render = (Component) => {
  ReactDOM.render(
    <AppContainer>
      <Component store={store} history={history} />
    </AppContainer>,
    document.getElementById('react-root')
  );
};

render(Root);

if (module.hot) {
  module.hot.accept('./Root', () => { render(Root); });
}
