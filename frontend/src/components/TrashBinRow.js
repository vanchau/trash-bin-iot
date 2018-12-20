import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import TrashBinDetails from "./TrashBinDetails"

const TrashBinRow = (props) => {
    return (
      <tr>
        <td>
          <Router>
            <div>
              <button className="btn btn-light">
              <Link 
                to={'/trashbin/'+props.bin.id}>
                {props.bin.id}
              </Link>
              </button>
              <Route 
              exact path={'/trashbin/'+props.bin.id}
              component={TrashBinDetails}>
              </Route>
            </div>
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

/*const Details = () => {
  return(
    <TrashBinDetails/>
  );
}*/

  export default TrashBinRow;