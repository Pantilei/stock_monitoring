import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  link: {
    color: '#61dafb',
  },
}));

export default function CustomPage() {
  const classes = useStyles();

  return (
    <a className={classes.link} href='/admin'>
      Admin Dashboard
    </a>
  );
}
