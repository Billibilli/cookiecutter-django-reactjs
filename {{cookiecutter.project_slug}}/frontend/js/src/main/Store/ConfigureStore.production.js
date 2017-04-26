import { browserHistory } from 'react-router';
import { routerMiddleware } from 'react-router-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';


import rootReducer from '../reducers';


const enhancer = compose(
  // Middleware you want to use in production
  applyMiddleware(thunk),
  applyMiddleware(routerMiddleware(browserHistory)),
);

// Function to call to configure Redux store
const configureStore = (initialState) => {
  // Note: only Redux >= 3.1.0 supports passing enhancer as third argument
  // See: https://github.com/rackt/redux/releases/tag/v3.1.0
  return createStore(rootReducer, initialState, enhancer);
};


export default configureStore;
