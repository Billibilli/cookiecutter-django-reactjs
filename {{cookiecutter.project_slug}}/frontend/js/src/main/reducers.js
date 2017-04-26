import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';

// Import reducers here and place them into the reducers object


const rootReducer = combineReducers({
  routing: routerReducer
});


export default rootReducer;
