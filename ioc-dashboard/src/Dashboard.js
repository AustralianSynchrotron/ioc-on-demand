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
    maxWidth: 800,
    margin: '0 auto',
  }
}


const PV_SUFFIXES = [
  'RANDOM',
  'FAST_RANDOM',
  'X',
  'Y',
  'X_TIMES_Y',
  'SHORT_STRING',
  'LONG_STRING',
  'ALERT',
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
    const { values } = this.state
    return (
      <div style={styles.tableContainer}>
        <h1>{`IOC Prefix: ${ioc}`}</h1>
        <Table wrapperStyle={styles.table}>
          <TableHeader displaySelectAll={false} adjustForCheckbox={false}>
            <TableRow selectable={false}>
              <TableHeaderColumn>Name</TableHeaderColumn>
              <TableHeaderColumn>Value</TableHeaderColumn>
            </TableRow>
          </TableHeader>
          <TableBody displayRowCheckbox={false}>
            <PvRow name={`${ioc}:RANDOM`} value={values[`${ioc}:RANDOM`]} />
            <PvRow name={`${ioc}:FAST_RANDOM`} value={values[`${ioc}:FAST_RANDOM`]} />
            <PvRow name={`${ioc}:X`} value={values[`${ioc}:X`]} />
            <PvRow name={`${ioc}:Y`} value={values[`${ioc}:Y`]} />
            <PvRow name={`${ioc}:X_TIMES_Y`} value={values[`${ioc}:X_TIMES_Y`]} />
            <PvRow name={`${ioc}:SHORT_STRING`} value={values[`${ioc}:SHORT_STRING`]} />
            <PvRow name={`${ioc}:LONG_STRING`} value={values[`${ioc}:LONG_STRING`]} />
            <PvRow name={`${ioc}:ALERT`} value={values[`${ioc}:ALERT`]} />
          </TableBody>
        </Table>
      </div>
    )
  }

}


const PvRow = ({name, value}) => (
  <TableRow selectable={false}>
    <TableRowColumn>{name}</TableRowColumn>
    <TableRowColumn>{value}</TableRowColumn>
  </TableRow>
)
