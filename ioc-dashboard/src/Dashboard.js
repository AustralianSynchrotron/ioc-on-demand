import React, { Component } from 'react'
import logo from './logo.svg'
import './App.css'


export default class Dashboard extends Component {

  constructor (props) {
    super(props)
    this.state = {connected: false, values: {}}
  }

  componentWillMount () {
    this.setState({connected: false})
    this.socket = new WebSocket('ws://localhost:5678/')
    this.socket.onopen = (event) => { this.subscribe() }
    this.socket.onmessage = this.update.bind(this)
  }

  componentWillUnmount () {
    this.socket.close()
    this.setState({connected: false})
  }

  subscribe () {
    const { ioc } = this.props.params
    const message = {action: 'subscribe', name: `${ioc}:RAND`}
    this.socket.send(JSON.stringify(message))
  }

  update (event) {
    const {name, value} = JSON.parse(event.data)
    const existingValues = this.state.values
    this.setState({values: {...existingValues, [name]: value}})
  }

  render() {
    const { ioc } = this.props.params
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>IOC Dashboard</h2>
        </div>
        <p>
          <emph>{`${ioc}:RAND: `}</emph>
          <span>{this.state.values[`${ioc}:RAND`]}</span>
        </p>
      </div>
    )
  }

}
