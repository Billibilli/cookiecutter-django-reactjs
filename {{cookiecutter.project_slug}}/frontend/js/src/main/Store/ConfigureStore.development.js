import { browserHistory } from 'react-router';
import { routerMiddleware } from 'react-router-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import { createLogger } from 'redux-logger'
import thunk from 'redux-thunk';


import DevTools from '../Root/DevTools';
import rootReducer from '../reducers';


const enhancer = compose(
  // Middleware you want to use in development
  applyMiddleware(thunk, createLogger()),
  applyMiddleware(routerMiddleware(browserHistory)),
  // Required! Enable Redux DevTools with the monitors you chose
  DevTools.instrument()
);

// Function to call to configure Redux store
const configureStore = (initialState) => {
  // Note: only Redux >= 3.1.0 supports passing enhancer as third argument
  // See: https://github.com/rackt/redux/releases/tag/v3.1.0
  const store = createStore(rootReducer, initialState, enhancer);

  // Hot Reload reducers
  // Note: Requires Webpack or Browserify HMR to be enabled
  if (module.hot) {
    module.hot.accept('../reducers', () =>
      store.replaceReducer(require('../reducers').default)
    );
  }
  return store;
};


export default configureStore;
