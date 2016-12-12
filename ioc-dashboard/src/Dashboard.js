import React, { Component } from 'react'
import logo from './logo.svg'
import './App.css'

export default class Dashboard extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>IOC Dashboard</h2>
        </div>
        <p className="App-intro">
          {this.props.params.ioc}
        </p>
      </div>
    )
  }
}
