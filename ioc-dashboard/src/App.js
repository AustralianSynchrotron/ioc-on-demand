import React, { Component } from 'react'
import axios from 'axios'

import logo from './logo.svg'
import './App.css'


export default class App extends Component {

  constructor (props) {
    super(props)
    this.handleLaunch = this.handleLaunch.bind(this)
  }

  handleLaunch () {
    axios.post('http://localhost:8080/new')
         .then(({ data }) => { this.props.router.push(`/${data}`) })
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>IOC Dashboard</h2>
        </div>
        <p className="App-intro">
          <button onClick={this.handleLaunch}>Launch IOC</button>
        </p>
      </div>
    )
  }
}
