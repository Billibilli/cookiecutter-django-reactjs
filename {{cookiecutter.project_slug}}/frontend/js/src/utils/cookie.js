import cookies from 'react-cookie';


// This is the place where we can load elements from a cookie to be used in our app
// Django CRSF Token is stored in a cookie
const csrftoken = cookies.load('csrftoken');

// This is not good practice, I need to find a way around using JWT from cookie to check user auth state
// django-rest-framework-jwt has a version coming soon to support using cookies. Once released we can turn this off
// https://github.com/sangoma/django-rest-framework-jwt/commit/947dde21c15544d313b10b8927950c2fb3a59405
// JWT SHOULD be saved into cookie
// This will happen in the loginUser actionCreator (look below):
// cookies.save('jwt', response.data.token, { secure: true, httpOnly: true });
// Therefore it will automatically be sent in the header of all API requests
// JWT will NOT be accessible to JavaScript because it is httpOnly :)

const jwt = cookies.load('jwt');

export { csrftoken, jwt };
