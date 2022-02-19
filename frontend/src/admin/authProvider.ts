import decodeJwt from 'jwt-decode';
import { BACKEND_URL } from '../config/index';

interface ILoginFormType {
  username: string;
  password: string;
}

const authProvider = {
  login: ({ username, password }: ILoginFormType) => {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    const request = new Request(`${BACKEND_URL}/login/access-token`, {
      method: 'POST',
      body: formData,
    });
    return fetch(request)
      .then((response) => {
        if (response.status < 200 || response.status >= 300) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then(({ access_token: accessToken }) => {
        const decodedToken: any = decodeJwt(accessToken);

        localStorage.setItem('token', accessToken);
        localStorage.setItem('scopes', decodedToken.scopes);
      });
  },
  logout: () => {
    localStorage.removeItem('token');
    localStorage.removeItem('permissions');
    return Promise.resolve();
  },
  checkError: (error: { status: number }) => {
    const { status } = error;
    if (status === 401 || status === 403) {
      localStorage.removeItem('token');
      return Promise.reject();
    }
    return Promise.resolve();
  },
  checkAuth: () =>
    localStorage.getItem('token') ? Promise.resolve() : Promise.reject(),
  getPermissions: () => {
    const role = localStorage.getItem('permissions');
    return role ? Promise.resolve(role) : Promise.reject();
  },
  //   getIdentity: () => {
  //     try {
  //       const { id, fullName, avatar } = JSON.parse(
  //         localStorage.getItem('identity') || ''
  //       );
  //       return Promise.resolve({ id, fullName, avatar });
  //     } catch (error) {
  //       return Promise.reject(error);
  //     }
  //   },
};

export default authProvider;
