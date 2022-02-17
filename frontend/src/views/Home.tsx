import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  link: {
    color: '#61dafb',
  },
}));

export default function Home() {
  const [message, setMessage] = useState<string>('');
  const [error, setError] = useState<string>('');
  const classes = useStyles();

  return (
    <>
      <a className={classes.link} href='/admin'>
        Admin Dashboard
      </a>
      <a className={classes.link} href='/protected'>
        Protected Route
      </a>
    </>
  );
}
