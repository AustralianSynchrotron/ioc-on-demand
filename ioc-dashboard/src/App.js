import React, { Component } from 'react'
import axios from 'axios'
import RaisedButton from 'material-ui/RaisedButton'


const styles = {
  container: {
    textAlign: 'center',
    paddingTop: 200,
  },
}

export default class App extends Component {

  constructor (props) {
    super(props)
    this.handleLaunch = this.handleLaunch.bind(this)
  }

  handleLaunch () {
    axios.post(`${process.env.REACT_APP_LAUNCH_URL}/new`)
         .then(({ data }) => { this.props.router.push(`/${data}`) })
  }

  render() {
    return (
      <div style={styles.container}>
        <h1>IOC Dashboard</h1>
        <RaisedButton label="Launch IOC" onTouchTap={this.handleLaunch} primary={true}/>
      </div>
    )
  }

}
