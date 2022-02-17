import React from 'react';
import {
  Create,
  SimpleForm,
  TextInput,
  PasswordInput,
  BooleanInput,
} from 'react-admin';

export default function UserCreate(props: any): React.ReactElement {
  return (
    <Create {...props}>
      <SimpleForm>
        <TextInput source='email' />
        <PasswordInput source='password' />
        <BooleanInput source='is_superuser' />
        <BooleanInput source='is_active' />
      </SimpleForm>
    </Create>
  );
}
