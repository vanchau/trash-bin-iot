import React from 'react';
import './styles.css'
import BioWasteIcon from '../../static/biowaste.png';
import CardBoardIcon from '../../static/carton.png';
import MetalIcon from '../../static/metal.png';
import GeneralIcon from '../../static/general.png';
import GlassIcon from '../../static/glass.png';
import PlasticIcon from '../../static/plastic.png'

const imageMap = {
  Biowaste: BioWasteIcon,
  Cardboard: CardBoardIcon,
  Metal: MetalIcon,
  General: GeneralIcon,
  Glass: GlassIcon,
  Plastic: PlasticIcon,
}

const getIconBackground = (type, fillStatus) => ((fillStatus === 100) ? (`${ type.toLowerCase() }-full`) : 'bin-ok')

const InfoBoxItem = ({ type, fillStatus }) => (
    <div>
        <img src={ imageMap[ type ] } className={ getIconBackground(type, fillStatus) } alt="test" />
    </div>
)
export default InfoBoxItem;
