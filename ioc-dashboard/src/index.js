import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, browserHistory } from 'react-router'

import App from './App'
import Dashboard from './Dashboard'
import './index.css'


const Routes = (props) => (
  <Router {...props}>
    <Route path="/" component={App}/>
    <Route path="/:ioc" component={Dashboard}/>
  </Router>
)


ReactDOM.render(
  <Routes history={browserHistory} />,
  document.getElementById('root')
)
