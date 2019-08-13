import React from 'react';
import './Item.css';
import Accordion from 'react-bootstrap/Accordion'
import Card from 'react-bootstrap/Card'
import Badge from 'react-bootstrap/Badge'
import Button from 'react-bootstrap/Button'
import moment from 'moment'

class Item extends React.Component {
    constructor(props) {

        super(props);
        this.item = props.item;

    }

    render() {

        const isCredit = (item) => {
            return item.type === 'CREDIT';
        };

        const date = moment(this.item.effectiveDate).format("YYYY/MM/DD HH:mm:ss");


        return (

            <Card className="itemCard">
                <Accordion.Toggle as={Card.Header} variant="link" eventKey={ this.item.id }>
                    <div class="container">
                        <div class="row">
                            <Badge variant={isCredit(this.item) ? 'success' : 'danger'}>{ this.item.type }</Badge>
                            <div class="col-sm">{ date }</div>
                            <div class="col-sm">{ this.item.description }</div>
                            <div className={isCredit(this.item) ? 'col-sm ammount positive' : 'col-sm ammount negative'}>{ this.item.ammount }</div>
                        </div>
                    </div>

                </Accordion.Toggle>

                <Accordion.Collapse eventKey={ this.item.id }>
                    <Card.Body>
                        <div>Id: { this.item.id }</div>
                        <div>Date: { date }</div>
                        <div>Ammount: { this.item.ammount }</div>
                        <div>Type: { this.item.type }</div>
                        <div>Description: { this.item.description }</div>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>

        );

    }
}

export default Item;