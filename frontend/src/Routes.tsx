import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { useHistory } from 'react-router';
import { makeStyles } from '@material-ui/core/styles';

import { Home, CustomPage } from './views';
import Admin from './admin';

const useStyles = makeStyles((theme) => ({
  app: {
    textAlign: 'center',
  },
  header: {
    backgroundColor: '#282c34',
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 'calc(10px + 2vmin)',
    color: 'white',
  },
}));

export default function Routes() {
  const classes = useStyles();
  const history = useHistory();

  return (
    <Switch>
      <Route path='/admin'>
        <Admin />
      </Route>

      <div className={classes.app}>
        <header className={classes.header}>
          <Route path='/custom-page' component={CustomPage} />
          <Route exact path='/' component={Home} />
        </header>
      </div>
    </Switch>
  );
}
