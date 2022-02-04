import React from 'react';
import {
  Edit,
  EditProps,
  SimpleForm,
  TextInput,
  BooleanInput,
  PasswordInput,
} from 'react-admin';

const UserEdit = (props: EditProps): React.ReactElement => {
  return (
    <Edit {...props}>
      <SimpleForm>
        <TextInput source='id' disabled />
        <TextInput source='email' />
        <PasswordInput source='password' />
        <BooleanInput source='is_active' />
        <BooleanInput source='is_superuser' />
      </SimpleForm>
    </Edit>
  );
};

export default UserEdit;
