import React from 'react';
import { Admin as ReactAdmin, Resource } from 'react-admin';
import authProvider from './authProvider';
import dataProvider from './dataProvider';

import { UserCreate, UserList, UserEdit } from './Users';

export default function Admin() {
  return (
    <ReactAdmin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource
        name='users'
        list={UserList}
        edit={UserEdit}
        create={UserCreate}
      />
    </ReactAdmin>
  );
}
