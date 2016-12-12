import React, { Component } from 'react'
import {
  Table, TableBody, TableHeader, TableHeaderColumn, TableRow, TableRowColumn
} from 'material-ui/Table'


const styles = {
  tableContainer: {
    textAlign: 'center',
    paddingTop: 50,
  },
  table: {
    maxWidth: 500,
    margin: '0 auto',
  }
}


const PV_SUFFIXES = [
  'RANDOM',
  'FAST_RANDOM',
]


export default class Dashboard extends Component {

  constructor (props) {
    super(props)
    this.state = {connected: false, values: {}}
  }

  componentWillMount () {
    this.setState({connected: false})
    this.socket = new WebSocket(process.env.REACT_APP_WS_URL)
    this.socket.onopen = (event) => { this.subscribe() }
    this.socket.onmessage = this.update.bind(this)
  }

  componentWillUnmount () {
    this.socket.close()
    this.setState({connected: false})
  }

  subscribe () {
    const { ioc } = this.props.params
    for (let suffix of PV_SUFFIXES) {
      const message = {action: 'subscribe', name: `${ioc}:${suffix}`}
      this.socket.send(JSON.stringify(message))
    }
  }

  update (event) {
    const {name, value} = JSON.parse(event.data)
    const existingValues = this.state.values
    this.setState({values: {...existingValues, [name]: value}})
  }

  render() {
    const { ioc } = this.props.params
    return (
      <div style={styles.tableContainer}>
        <h1>{`IOC: ${ioc}`}</h1>
        <Table wrapperStyle={styles.table}>
          <TableHeader displaySelectAll={false} adjustForCheckbox={false}>
            <TableRow>
              <TableHeaderColumn>Name</TableHeaderColumn>
              <TableHeaderColumn>Value</TableHeaderColumn>
            </TableRow>
          </TableHeader>
          <TableBody displayRowCheckbox={false}>
            <TableRow>
              <TableRowColumn>{`${ioc}:RANDOM`}</TableRowColumn>
              <TableRowColumn>{this.state.values[`${ioc}:RANDOM`]}</TableRowColumn>
            </TableRow>
            <TableRow>
              <TableRowColumn>{`${ioc}:FAST_RANDOM`}</TableRowColumn>
              <TableRowColumn>{this.state.values[`${ioc}:FAST_RANDOM`]}</TableRowColumn>
            </TableRow>
          </TableBody>
        </Table>
      </div>
    )
  }

}
