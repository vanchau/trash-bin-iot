import React from 'react'
import { compose, withProps } from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap,
} from 'react-google-maps';
import MarkerWithInfoBox from '../MarkerWithInfoBox'
import { getMarkerUrl, getScaledMarkerSize, getOverflowTypes } from '../../utils'

const styledMap = require('./styledMap.json')
const locationOverflow = require('../../static/location-full.png')
const locationOk = require('../../static/location-ok.png')
const locationOverflowAndLate = require('../../static/location-late-pickup.png')

const key = process.env.REACT_APP_GOOGLE_API_KEY !== null ? process.env.REACT_APP_GOOGLE_API_KEY : '';

const getTrashBins = bins => bins.map(bin => ({ type: bin.wasteType, fillStatus: bin.fillStatus }))

const GoogleMaps = compose(
  withProps({
    googleMapURL: `https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${key}`, // add google maps api key to the end of the line.
    loadingElement: <div style={ { height: '100%' } } />,
    containerElement: <div style={ { height: '100%' } } />,
    mapElement: <div style={ { height: '100%' } } />,
  }),

  withScriptjs,
  withGoogleMap,
)( props => (
    <GoogleMap
      defaultZoom={ 16 }
      defaultCenter={ {
        lat: 60.1873,
        lng: 24.82339,
      } }
      defaultOptions={ {
        styles: styledMap,
        streetViewControl: false,
        mapTypeControl: false,
        fullscreenControl: false,
      } } // load custom map style and disable street view
    >
        { props.locations.map( location => ( // map locations and statuses to create markers
            <MarkerWithInfoBox
              icon={ {
                url: getMarkerUrl(location, locationOk, locationOverflow, locationOverflowAndLate),
                title: '',
                scaledSize: getScaledMarkerSize(location),
              } }
              position={ {
                lat: location.lat,
                lng: location.lon,
              } }
              trashBins={ getTrashBins(location.trashbins) }
              key={ location.id }
              locationId={ location.id }
              address={ location.address }
              toggleLocationView={ props.toggleLocationView }
              overflowTypes={ getOverflowTypes(location) }
            />
        ))}

    </GoogleMap>
));

// Export Google Map component
export default GoogleMaps
