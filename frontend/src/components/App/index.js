import React, { Component } from 'react';
import './styles.css';
import FilterContainer from '../FilterContainer'
import GoogleMaps from '../GoogleMaps'

const aaltoLocations = require('../../api/aalto-with-trashbins.json')

const locationTrashBins = aaltoLocations.map(
  loc => loc.trashbins,
).map(trashbin => trashbin.map(bin => ( bin.wasteType)));


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      typeFilters: new Map(),
      statusFilters: new Map(),
    };
    this.onTypeFilterChange = this.onTypeFilterChange.bind(this);
    this.onStatusFilterChange = this.onStatusFilterChange.bind(this);
  }

  onTypeFilterChange(item, isChecked) {
    this.setState(prevState => ({ typeFilters: prevState.typeFilters.set(item, isChecked) }));
  }

  onStatusFilterChange(item, isChecked) {
    this.setState(prevState => ({ statusFilters: prevState.statusFilters.set(item, isChecked) }));
  }

  getFilteredLocations(typeFilters, statusFilters) {
	  console.log(typeFilters);
    const checkedTypeFilters = new Map([ ...typeFilters ].filter(([ , value ]) => value === true));
    const checkedStatusFilters = new Map([ ...statusFilters ].filter(([ , value ]) => value === true));
    const toRender = [ ...checkedTypeFilters.keys(), ...checkedStatusFilters.keys() ];
	console.log(this.state.statusFilters.get("Late pickups"))
    const locations = [];

    locationTrashBins.forEach((loc, i) => {
      if (toRender.length === 0
        || toRender.filter(value => loc.indexOf(value) !== -1).length > 0) {
        locations.push(aaltoLocations[ i ])
      }
    })

    return this.getOverdueLocations(locations);
  }
  
  getOverdueLocations(locations) {
	var ret = locations.filter(a => a.trashbins.filter(c => c.pickupOverdue === true).length !== 0 );
	
    return ret;
  }



  render() {
    const { typeFilters, statusFilters } = this.state;
    return (
        <div className="fluid-container">
            <FilterContainer
              onTypeFilterChange={ this.onTypeFilterChange }
              typeFilters={ typeFilters }
              onStatusFilterChange={ this.onStatusFilterChange }
              statusFilters={ statusFilters }
            />
            <div className="map">
                <GoogleMaps
                  locations={ this.getFilteredLocations(typeFilters, statusFilters) }
                />
            </div>
        </div>
    );
  }
}

export default App;
