import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, browserHistory } from 'react-router'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import injectTapEventPlugin from 'react-tap-event-plugin'

import App from './App'
import Dashboard from './Dashboard'
import './style.css'


injectTapEventPlugin()


const Routes = (props) => (
  <MuiThemeProvider>
    <Router {...props}>
      <Route path="/" component={App}/>
      <Route path="/iocs/:ioc" component={Dashboard}/>
    </Router>
  </MuiThemeProvider>
)


ReactDOM.render(
  <Routes history={browserHistory} />,
  document.getElementById('root')
)
