import { fetchUtils, HttpError } from 'react-admin';
import {
  DataProvider,
  GetOneParams,
  GetListParams,
  GetManyParams,
  GetManyReferenceParams,
  UpdateParams,
  UpdateManyParams,
  CreateParams,
  DeleteParams,
  DeleteManyParams,
} from 'ra-core';
import { stringify } from 'query-string';
import { BACKEND_URL } from '../config/index';

const apiUrl = BACKEND_URL;

export interface Options extends RequestInit {
  user?: {
    authenticated?: boolean;
    token?: string;
  };
}

export const createHeadersFromOptions = (options: Options): Headers => {
  const requestHeaders = (options.headers ||
    new Headers({
      Accept: 'application/json',
    })) as Headers;
  if (
    !requestHeaders.has('Content-Type') &&
    !(options && (!options.method || options.method === 'GET')) &&
    !(options && options.body && options.body instanceof FormData)
  ) {
    requestHeaders.set('Content-Type', 'application/json');
  }
  if (options.user && options.user.authenticated && options.user.token) {
    requestHeaders.set('Authorization', options.user.token);
  }

  return requestHeaders;
};

export const fetchJson = (url: any, options: Options = {}) => {
  const requestHeaders = createHeadersFromOptions(options);
  return fetch(url, { ...options, headers: requestHeaders })
    .then((response) => {
      console.log('response: text ', response.statusText);
      console.log('GGGG headers: ', Array.from(response.headers));
      return response.text().then((text) => ({
        status: response.status,
        statusText: response.statusText,
        headers: response.headers,
        body: text,
      }));
    })
    .then(({ status, statusText, headers, body }) => {
      let json;
      try {
        json = JSON.parse(body);
      } catch (e) {
        // not json, no big deal
      }
      if (status < 200 || status >= 300) {
        return Promise.reject(
          new HttpError((json && json.message) || statusText, status, json)
        );
      }
      return Promise.resolve({ status, headers, body, json });
    });
};

const httpClient = (
  url: string,
  options: { [field_name: string]: any } = {}
) => {
  let { headers } = options;
  if (!headers) {
    headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  headers.set('Authorization', `Bearer ${token}`);

  // return fetchUtils.fetchJson(url, { ...options, headers });
  return fetchJson(url, { ...options, headers });
};

const dataProvider: DataProvider = {
  getList: (resource: string, params: GetListParams) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify(params.filter),
    };
    const url = `${apiUrl}/${resource}?${stringify(query)}`;

    return httpClient(url).then((res) => {
      console.log(res);

      const { headers, json } = res;
      const contentRange = headers.get('content-range');
      if (!contentRange) {
        return Promise.reject(new Error('content-range header is missing!'));
      }
      return Promise.resolve({
        data: json,
        total: parseInt(contentRange.split('/').pop() || '', 10),
      });
    });
  },

  getOne: (resource: string, params: GetOneParams) =>
    httpClient(`${apiUrl}/${resource}/${params.id}`).then(({ json }) => ({
      data: json,
    })),

  getMany: (resource: string, params: GetManyParams) => {
    const query = {
      filter: JSON.stringify({ ids: params.ids }),
    };
    const url = `${apiUrl}/${resource}?${stringify(query)}`;
    return httpClient(url).then(({ json }) => ({ data: json }));
  },

  getManyReference: (resource: string, params: GetManyReferenceParams) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify({
        ...params.filter,
        [params.target]: params.id,
      }),
    };
    const url = `${apiUrl}/${resource}?${stringify(query)}`;

    return httpClient(url).then(({ headers, json }) => {
      const contentRange = headers.get('content-range');
      if (!contentRange) {
        return Promise.reject(new Error('content-range header is missing!'));
      }
      return Promise.resolve({
        data: json,
        total: parseInt(contentRange.split('/').pop() || '', 10),
      });
    });
  },

  update: (resource: string, params: UpdateParams) =>
    httpClient(`${apiUrl}/${resource}/${params.id}`, {
      method: 'PUT',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({ data: json })),

  updateMany: (resource: string, params: UpdateManyParams) => {
    const query = {
      filter: JSON.stringify({ id: params.ids }),
    };
    return httpClient(`${apiUrl}/${resource}?${stringify(query)}`, {
      method: 'PUT',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({ data: json }));
  },

  create: (resource: string, params: CreateParams) =>
    httpClient(`${apiUrl}/${resource}`, {
      method: 'POST',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({
      data: { ...params.data, id: json.id },
    })),

  delete: (resource: string, params: DeleteParams) =>
    httpClient(`${apiUrl}/${resource}/${params.id}`, {
      method: 'DELETE',
    }).then(({ json }) => ({ data: json })),

  deleteMany: (resource: string, params: DeleteManyParams) => {
    const query = {
      filter: JSON.stringify({ id: params.ids }),
    };
    return httpClient(`${apiUrl}/${resource}?${stringify(query)}`, {
      method: 'DELETE',
    }).then(({ json }) => ({ data: json }));
  },
};

export default dataProvider;
