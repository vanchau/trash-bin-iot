import React from 'react';
import { Marker } from 'react-google-maps';
import './styles.css'
import LocationSummaryItem from './LocationSummaryItem';

const { InfoBox } = require('react-google-maps/lib/components/addons/InfoBox');



class MarkerWithInfoWindow extends React.Component {
  constructor() {
    super();
    this.state = {
      isOpen: false,
    }
    this.onToggleOpen = this.onToggleOpen.bind(this);
  }

  onToggleOpen() {
    const { isOpen } = this.state
    this.setState({
      isOpen: !isOpen,
    });
  }

  render() {
    const { position, icon, trashBins} = this.props
    const { isOpen } = this.state
    console.log(trashBins)
    return (
        <Marker
          position={ position }
          onMouseOver={ this.onToggleOpen }
          onMouseOut={ this.onToggleOpen }
          onFocus={ this.onToggleOpen }
          onBlur={ this.onToggleOpen }
          icon={ icon }
        >
            { isOpen && (
            <InfoBox
              defaultPosition={ new window.google.maps.LatLng(position.lat, position.lng) }
              options={ {
                pixelOffset: new window.google.maps.Size(-10, -200),
                closeBoxURL: '',
              } }
            >
                <div className="box triangle">
                {
                  trashBins.map(bin => (
                    <LocationSummaryItem
                    type={bin.type}
                    fillStatus={bin.fillStatus}
                  />
                  ))
                }
                  
                </div>
            </InfoBox>
            )}
        </Marker>
    )
  }
}

export default MarkerWithInfoWindow;
