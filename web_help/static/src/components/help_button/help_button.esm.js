/** @odoo-module **/
import LegacyControlPanel from "web.ControlPanel";
import {ControlPanel} from "@web/search/control_panel/control_panel";
import {findTrip} from "@web_help/helpers.esm";
import {Component, useState} from "@odoo/owl";
import {ActionDialog} from "@web/webclient/actions/action_dialog";

export class HelpButton extends Component {
    setup() {
        const foundTrip = findTrip(this.props.resModel, this.props.viewType);
        this.state = useState({
            TripClass: foundTrip,
        });
    }

    onClick() {
        const TripClass = this.state.TripClass;
        const trip = new TripClass(this.env);
        trip.setup();
        trip.start();
    }
}

HelpButton.template = "web_help.HelpButton";

Object.assign(ControlPanel.components, {HelpButton});
Object.assign(LegacyControlPanel.components, {HelpButton});
Object.assign(ActionDialog.components, {HelpButton});
