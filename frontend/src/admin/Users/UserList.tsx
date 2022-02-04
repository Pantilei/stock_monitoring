import React from 'react';
import {
  List,
  ListProps,
  Datagrid,
  TextField,
  BooleanField,
  EmailField,
  EditButton,
} from 'react-admin';

const UserList = (props: ListProps): React.ReactElement => {
  return (
    <List {...props}>
      <Datagrid rowClick='edit'>
        <TextField source='id' />
        <EmailField source='email' />
        <EditButton />
      </Datagrid>
    </List>
  );
};

export default UserList;
