import React from 'react';
import { Route, IndexRoute } from 'react-router';
import PropTypes from 'prop-types';

import * as cookie from '../utils/cookie';


// Placeholder - Hello World! :)
const HelloWorld = () =>
  <div>
    <h1>Hello World!</h1>
  </div>;


const routes = (
  <div>
    <Route path="/" component={HelloWorld} />
  </div>
);


export default routes;
