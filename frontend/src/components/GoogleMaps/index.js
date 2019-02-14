import React from 'react'
import { compose, withProps, withStateHandlers } from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap, Marker,
} from 'react-google-maps';

const trashbin = require('../../static/trashbin.png')

const GoogleMaps = compose(
  withProps({
    googleMapURL: 'https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=', // add google maps api key to the end of the line.
    loadingElement: <div style={ { height: '100%' } } />,
    containerElement: <div style={ { height: '100%' } } />,
    mapElement: <div style={ { height: '100%' } } />,
  }),
  withStateHandlers(() => ({
    isOpen: false,
  }), {
    onToggleOpen: ({ isOpen }) => () => ({
      isOpen: !isOpen,
    }),
  }),
  withScriptjs,
  withGoogleMap,
)( props => (
    <GoogleMap
      defaultZoom={ 14 }
      defaultCenter={ {
        lat: 60.1873,
        lng: 24.82339,
      } }
    >

        { props.locations.map( marker => (
            <Marker
              icon={ {
                url: trashbin,
                title: 'trashbin',
                scaledSize: new window.google.maps.Size(35, 40),
              } }
              position={ {
                lat: marker.lat,
                lng: marker.lon,
              } }
              key={ marker.id }
            />
        ))}

    </GoogleMap>
));

// Export Google Map component
export default GoogleMaps