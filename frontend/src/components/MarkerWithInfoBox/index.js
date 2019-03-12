import React from 'react';
import { Marker } from 'react-google-maps';
import './styles.css'
import InfoBoxItem from '../InfoBoxItem';

const { InfoBox } = require('react-google-maps/lib/components/addons/InfoBox');

class MarkerWithInfoBox extends React.Component {
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

  offsetCounter(trashBins, markerSize) {
    return (-100 - (Math.ceil(trashBins.length / 4)) * 65 - markerSize.height + 15)
  }

  render() {
    const { isOpen } = this.state;
    const {
      position, icon, trashBins, toggleLocationView, locationId,
    } = this.props;
    let { address } = this.props;
    address = address.split(',')[ 0 ].toLowerCase()
    address = address.charAt(0).toUpperCase() + address.slice(1)
    return (
        <Marker
          position={ position }
          onMouseOver={ this.onToggleOpen }
          onMouseOut={ this.onToggleOpen }
          onFocus={ this.onToggleOpen }
          onBlur={ this.onToggleOpen }
          icon={ icon }
          onClick={ () => toggleLocationView(locationId) }
        >
            { isOpen && (
            <InfoBox
              defaultPosition={ new window.google.maps.LatLng(position.lat, position.lng) }
              options={ {
                pixelOffset:
                  new window.google.maps.Size(-10, this.offsetCounter(trashBins, icon.scaledSize)),
                closeBoxURL: '', // set to "null" as it's closed on hover
              } }
            >
                <div className="box triangle">
                    <div className="dark-teal-infobox">
                        <p className="address-text">{address}</p>
                    </div>
                    <div className="type-icon-container">
                        {
                      trashBins.map((bin, i) => (
                          <InfoBoxItem
                            type={ bin.type }
                            fillStatus={ bin.fillStatus }
                            key={ i }
                          />
                      ))
                    }
                    </div>
                </div>
            </InfoBox>
            )}
        </Marker>
    )
  }
}

export default MarkerWithInfoBox;
