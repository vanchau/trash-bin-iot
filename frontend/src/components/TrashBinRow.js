import React from 'react';
import { BrowserRouter as Router, Link } from "react-router-dom";

const TrashBinRow = (props) => {
    return (
      <tr>
        <td>
        <Router>
        <Link to={props.bin.id} onClick={() => props.setBinSelected(props.bin)}>
          <button className="btn btn-light">
            {props.bin.id}
          </button>
        </Link>
        </Router>
        </td>
        <td>{props.bin.owner}</td>
        <td>{props.bin.address}</td>
        <td>{props.bin.bintype}</td>
        <td>{props.bin.latestEvent}</td>
        
        {props.status === "OK" ? (
        <td className="text-success">{props.bin.status}</td> ) :
        (<td className="text-danger">{props.bin.status}</td>)
        }
      </tr>
    )
  }

  export default TrashBinRow;